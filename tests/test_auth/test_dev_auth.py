class TestDevAuth:
    '''DevAuth handling'''

    authorized_uid = '2040'

    def test_disabled(self, app, client):
        '''blocks access unless enabled'''
        app.config['DEVELOPER_AUTH_ENABLED'] = False
        response = client.get('/devauth/login')
        assert response.status_code == 403
        response = client.post('/devauth/login', data={'uid': self.authorized_uid, 'password': app.config['DEVELOPER_AUTH_PASSWORD']})
        assert response.status_code == 403

    def test_enabled(self, app, client):
        '''supports login forms when enabled'''
        app.config['DEVELOPER_AUTH_ENABLED'] = True
        response = client.get('/devauth/login')
        assert response.status_code == 200
        assert response.content_type.startswith('text/html')
        assert '<form' in str(response.data)

    def test_password_fail(self, app, client):
        '''fails if no match on developer password'''
        app.config['DEVELOPER_AUTH_ENABLED'] = True
        response = client.post('/devauth/login', data={'uid': self.authorized_uid, 'password': 'Born 2 Lose'})
        assert response.status_code == 403

    def test_authorized_user_fail(self, app, client):
        '''fails if the chosen UID does not match an authorized user'''
        app.config['DEVELOPER_AUTH_ENABLED'] = True
        response = client.post('/devauth/login', data={'uid': 'A Bad Sort', 'password': app.config['DEVELOPER_AUTH_PASSWORD']})
        assert response.status_code == 403

    def test_known_user_with_correct_password_logs_in(self, app, client):
        '''there is a happy path'''
        app.config['DEVELOPER_AUTH_ENABLED'] = True
        response = client.post('/devauth/login', data={'uid': self.authorized_uid, 'password': app.config['DEVELOPER_AUTH_PASSWORD']})
        assert response.status_code == 302
        response = client.get('/api/status')
        assert response.status_code == 200
        assert self.authorized_uid in str(response.data)
        response = client.get('/logout')
        assert response.status_code == 302
        response = client.get('/api/status')
        assert response.status_code == 200
        assert 'Anonymous' in str(response.data)
