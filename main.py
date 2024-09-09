from flask import Flask
from configuration import configure_all

#inicializando
app = Flask(__name__)

#rotas
configure_all(app)
#executar o código
app.run(debug=True)