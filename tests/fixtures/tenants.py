import pytest

from snakeskin.models.tenant import Tenant


@pytest.fixture
def fixture_tenants(db_session):
    ucb = Tenant(name='UC Berkeley')
    ucoe = Tenant(name='UC Online Education')
    db_session.add(ucb)
    db_session.add(ucoe)
    db_session.commit()

    return [ucb, ucoe]
