from routes.home import home_route
from routes.clientes import cliente_route
from Database.Models.cliente import conectar_banco

def configure_all(app):
    configure_routes(app)
    configure_db()
    
def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configure_db():
    conectar_banco()