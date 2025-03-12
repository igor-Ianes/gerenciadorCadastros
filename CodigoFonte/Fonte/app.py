from flask import Flask
from controladores.cadastros import setup_routes
from controladores.update_profissional import setup_update_routes
from controladores.consultar_disponibilidade import setup_consultar_disponibilidade_routes

app = Flask(__name__)

setup_routes(app) 
setup_update_routes(app) 
setup_consultar_disponibilidade_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
