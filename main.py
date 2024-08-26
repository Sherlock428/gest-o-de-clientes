from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.clientes import cliente_route
#inicializando
app = Flask(__name__)


#rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')
#executar o código
app.run(debug=True)