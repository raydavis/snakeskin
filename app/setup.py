from flask import make_response


def load_configs(app):
    # Load default configs.
    app.config.from_object('config.default')
    # Load local configs not under version control.
    app.config.from_object('config.development-local')

def register_routes(app):
    # Register API routes as blueprints.
    from app.api.tenant_controller import tenant
    from app.api.user_controller import user

    app.register_blueprint(tenant)
    app.register_blueprint(user)

    # Routes not matched by the API are handled by the front end.
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def front_end_route(**kwargs):
        return make_response(open('app/templates/index.html').read())
