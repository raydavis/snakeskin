import pytest
import sqlalchemy.exc

from snakeskin.models.tenant import Tenant


class TestTenant:
    '''Tenant model'''
    def test_query(self, db_session, fixture_tenants):
        '''can be queried'''
        tenants = Tenant.query.all()
        assert len(tenants) == 2

    def test_requires_name(self, db_session):
        '''raises a database error if a name is not provided'''
        with pytest.raises(sqlalchemy.exc.IntegrityError):
            tenant = Tenant(name=None)
            db_session.add(tenant)
            db_session.commit()

    def test_receives_id_on_creation(self, db_session):
        '''receives a numeric ID on creation'''
        tenant = Tenant(name='University of Life')
        db_session.add(tenant)
        assert tenant.id is None

        db_session.commit()
        assert tenant.id > 0
