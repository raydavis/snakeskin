import os
import pytest
import subprocess

from app import factory

from tests.fixtures.tenants import *

os.environ['SNAKESKIN_ENV'] = 'test'


@pytest.fixture(scope='session')
def app(request):
    '''Fixture application object.'''
    _app = factory.create_app()
    factory.register_routes(_app)

    # Create app context before running tests.
    ctx = _app.app_context()
    ctx.push()

    # Pop the context after running tests.
    def teardown():
        ctx.pop()
    request.addfinalizer(teardown)

    return _app


@pytest.fixture(scope='session')
def db(app, request):
    '''Fixture database object.'''
    _db = factory.initialize_db(app)
    _db.app = app

    # The psycopg2 engine doesn't handle big pg_dump files well, so shell out to load the schema. Abort the
    # transaction and test suite if the schema contains errors.
    load_schema_cmd = 'psql -v ON_ERROR_STOP=ON --single-transaction snakeskin_test < scripts/db/schema.sql'
    subprocess.check_output(load_schema_cmd, shell=True)

    # Drop all tables after running tests.
    def teardown():
        r = _db.engine.execute("SELECT tablename FROM pg_tables where schemaname='public'")
        table_names = [row[0] for row in r]
        _db.engine.execute('DROP TABLE IF EXISTS {} CASCADE'.format(', '.join(table_names)))
    request.addfinalizer(teardown)

    return _db


@pytest.fixture(scope='function')
def db_session(db, request):
    '''
    Fixture database session used for the scope of a single test. All executions are wrapped
    in a transaction and then rolled back to keep individual tests isolated.
    '''
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    _session = db.create_scoped_session(options=options)
    db.session = _session

    # Roll back transaction and close connection when the test is complete.
    def teardown():
        transaction.rollback()
        connection.close()
        _session.remove()
    request.addfinalizer(teardown)

    return _session


def pytest_itemcollected(item):
    '''Print docstrings during test runs for more readable output.'''
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
