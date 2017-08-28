from flask import make_response


def register_routes(app):
    """Register app routes."""

    # Register API routes as blueprints.
    from snakeskin.api.tenant_controller import tenant
    from snakeskin.api.user_controller import user
    app.register_blueprint(tenant)
    app.register_blueprint(user)
    import snakeskin.api.status_controller

    # Register authentication modules.
    from snakeskin.auth.authorized_user import login_manager
    login_manager.init_app(app)
    import snakeskin.auth.dev_auth
    import snakeskin.auth.cas_auth

    # Error handling.
    import snakeskin.api.errors

    # Unmatched API routes return a 404.
    @app.route('/api/<path:path>')
    def handle_unmatched_api_route(**kwargs):
        raise snakeskin.api.errors.ResourceNotFoundError('The requested resource could not be found.')

    # Non-API routes are handled by the front end.
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def front_end_route(**kwargs):
        return make_response(open('snakeskin/templates/index.html').read())
