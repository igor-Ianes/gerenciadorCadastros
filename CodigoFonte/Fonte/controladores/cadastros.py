from flask import render_template, request, redirect, url_for
from servicos.sistema_facade import SistemaFacade

sistema_facade = SistemaFacade()

def setup_routes(app):
    @app.route('/')
    def sistema():
        return render_template('sistema.html')

    @app.route('/cadastrar_profissionais')
    def cadastrar_profissionais():
        especialidades = sistema_facade.obter_especialidades_por_nome()
        return render_template('cadastrarProfissionais.html', especialidades=especialidades)

    @app.route('/cadastrar_especialidades')
    def cadastrar_especialidades():
        return render_template('cadastrarEspecialidades.html')

    @app.route('/submit', methods=['POST'])
    def submit():
        action = request.form.get('action')

        if action == 'Cadastrar profissionais':
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            contato = request.form.get("contato")
            especialidade_nome = request.form.get("especialidade")

            if not nome or not cpf or not contato:
                return "<h1>Erro: Campos obrigatórios não foram preenchidos</h1>"

            try:
                sistema_facade.cadastrar_profissional(nome, cpf, contato, especialidade_nome)
                return render_template('operacao_sucesso.html')
            except Exception as e:
                return f"<h1>Erro ao cadastrar Profissional</h1><p>{str(e)}</p>"

        elif action == 'Cadastrar especialidades':
            nome = request.form.get("nome")
            descricao = request.form.get("descricao")

            if not nome:
                return "<h1>Erro: O campo nome é obrigatório</h1>"

            try:
                sistema_facade.cadastrar_especialidade(nome, descricao)
                return render_template('operacao_sucesso.html')
            except Exception as e:
                return f"<h1>Erro ao cadastrar Especialidade</h1><p>{str(e)}</p>"

        elif action == 'Alterar informações de profissionais já cadastrados':
            return redirect(url_for('alterar_cadastro_route'))

        elif action == 'Consultar disponibilidade':
            return redirect(url_for('consultar_disponibilidade_route'))
