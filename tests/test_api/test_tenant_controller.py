class TestTenantController:
    '''Tenant API'''
    def test_tenants_list(self, client, fixture_tenants):
        '''returns a well-formed response'''
        response = client.get('/api/tenant/')
        assert response.status_code == 200
        assert len(response.json) == 2

        assert response.json[0]['id'] == fixture_tenants[0].id
        assert response.json[0]['name'] == 'UC Berkeley'

        assert response.json[1]['id'] == fixture_tenants[1].id
        assert response.json[1]['name'] == 'UC Online Education'

    def test_tenant_single(self, client, fixture_tenants):
        '''returns a single tenant'''
        response = client.get('/api/tenant/{}'.format(fixture_tenants[0].id))
        assert response.status_code == 200
        assert response.json['id'] == fixture_tenants[0].id
        assert response.json['name'] == 'UC Berkeley'

    def test_tenant_not_found(self, client, fixture_tenants):
        '''returns 404 for an unknown id'''
        response = client.get('/api/tenant/99999')
        assert response.status_code == 404
        assert response.json['message'] == 'The requested tenant could not be found.'
