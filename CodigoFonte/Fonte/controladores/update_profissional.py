from flask import render_template, request
from servicos.sistema_facade import SistemaFacade

sistema_facade = SistemaFacade()

def setup_update_routes(app):
    @app.route('/alterar_cadastro')
    def alterar_cadastro():
        profissionais = sistema_facade.obter_profissionais()
        return render_template('listarProfissionais.html', profissionais=profissionais)

    @app.route('/editar_profissional/<nome>')
    def editar_profissional(nome):
        profissional = sistema_facade.obter_profissional_por_nome(nome)
        especialidades = sistema_facade.obter_especialidades_por_nome()
        return render_template('editarProfissional.html', profissional=profissional, especialidades=especialidades)

    @app.route('/atualizar_profissional/<int:id>', methods=['POST'])
    def atualizar_profissional(id):
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        contato = request.form.get("contato")
        especialidade_nome = request.form.get("especialidade")

        if not nome or not cpf or not contato:
            return "<h1>Erro: Campos obrigatórios não foram preenchidos</h1>"

        try:
            sistema_facade.atualizar_profissional(id, nome, cpf, contato, especialidade_nome)
            return render_template('operacao_sucesso.html')
        except Exception as e:
            return f"<h1>Erro ao atualizar Profissional</h1><p>{str(e)}</p>"
