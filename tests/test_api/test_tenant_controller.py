class TestTenantController:
    '''Tenant API'''
    def test_tenant_api(self, client, fixture_tenants):
        '''returns a well-formed response'''
        response = client.get('/api/tenant/')
        assert response.status_code == 200
        assert len(response.json) == 2

        assert response.json[0]['id'] is not None
        assert response.json[0]['name'] == 'UC Berkeley'

        assert response.json[1]['id'] is not None
        assert response.json[1]['name'] == 'UC Online Education'
