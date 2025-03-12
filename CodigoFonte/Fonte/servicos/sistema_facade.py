from modelos.profissionais import Profissional, adicionar_profissional, obter_profissionais, obter_profissional_por_nome, atualizar_profissional
from modelos.especialidades import Especialidade, adicionar_especialidade, obter_especialidades_por_nome

# classe para simplificar a interação com os modelos de dados
class SistemaFacade:
    def cadastrar_profissional(self, nome, cpf, contato, especialidade_nome):
        especialidade = obter_especialidades_por_nome(especialidade_nome)
        especialidade_id = especialidade[0].id if especialidade else None
        profissional = Profissional(nome=nome, cpf=cpf, contato=contato, especialidade_id=especialidade_id)
        adicionar_profissional(profissional)

    def cadastrar_especialidade(self, nome, descricao):
        especialidade = Especialidade(nome=nome, descricao=descricao)
        adicionar_especialidade(especialidade)

    def obter_especialidades_por_nome(self, nome=None):
        return obter_especialidades_por_nome(nome)

    def obter_profissionais(self):
        return obter_profissionais()

    def obter_profissional_por_nome(self, nome):
        return obter_profissional_por_nome(nome)

    def atualizar_profissional(self, id, nome, cpf, contato, especialidade_nome):
        especialidade = obter_especialidades_por_nome(especialidade_nome)
        especialidade_id = especialidade[0].id if especialidade else None
        profissional = Profissional(id=id, nome=nome, cpf=cpf, contato=contato, especialidade_id=especialidade_id)
        atualizar_profissional(profissional)
