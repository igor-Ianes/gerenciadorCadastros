from flask import render_template, request
from modelos.disponibilidade import obter_disponibilidade

def setup_consultar_disponibilidade_routes(app):
    @app.route('/consultar_disponibilidade')
    def consultar_disponibilidade_route():
        return render_template('consultarDisponibilidade.html')

    @app.route('/resultado_disponibilidade', methods=['POST'])
    def resultado_disponibilidade_route():
        nome = request.form.get("nome")
        especialidade = request.form.get("especialidade")

        resultados = obter_disponibilidade(nome, especialidade)
        return render_template('resultadoDisponibilidade.html', resultados=resultados)
