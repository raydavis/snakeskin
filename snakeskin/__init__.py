from snakeskin import factory

app = factory.create_app()
db = factory.initialize_db(app)

# Route registration depends on the database being in place (because of dependencies on models).
factory.register_routes(app)
