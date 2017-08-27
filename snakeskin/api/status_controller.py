from flask import current_app, jsonify
from flask_login import current_user

@current_app.route('/api/status')
def app_status():
    authn_state = current_user
    return jsonify({
        'authenticated_as': repr(authn_state)
    })
