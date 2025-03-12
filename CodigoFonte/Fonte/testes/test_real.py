import unittest
from modelos.profissionais import Profissional, adicionar_profissional, obter_profissional_por_nome, obter_especialidades_por_nome
from modelos.especialidades import Especialidade, adicionar_especialidade

class TestDatabase(unittest.TestCase):

    def test_gravacao_profissional(self):
        # Obtendo o ID da especialidade
        especialidades = obter_especialidades_por_nome('Cardiologia')
        if not especialidades:
            self.fail("Especialidade 'Cardiologia' não encontrada no banco de dados.")
        especialidade_id = especialidades[0].id

        # Criando o profissional com todos os campos necessários preenchidos
        profissional = Profissional(nome="Dr. Lucio Mendes", cpf="736.836.827-55", contato="lucio.mendes@gmail.com", especialidade_id=especialidade_id)
        adicionar_profissional(profissional)

        # Verificando se o profissional foi salvo corretamente
        profissional_inserido = obter_profissional_por_nome(profissional.nome)
        
        self.assertIsNotNone(profissional_inserido)
        self.assertEqual(profissional_inserido.nome, profissional.nome)
        self.assertEqual(profissional_inserido.cpf, profissional.cpf)
        self.assertEqual(profissional_inserido.contato, profissional.contato)
        self.assertEqual(profissional_inserido.especialidade_id, profissional.especialidade_id)

    def test_duplicidade_especialidade(self):
        # Adicionando a especialidade "Emergencial"
        especialidade = Especialidade(nome="Emergencial", descricao="Especialidade em medicina emergencial")
        adicionar_especialidade(especialidade)

        # Tentando adicionar a mesma especialidade novamente e esperando um erro
        with self.assertRaises(Exception) as context:
            adicionar_especialidade(especialidade)
        
        self.assertIn("Duplicate entry", str(context.exception))

if __name__ == "__main__":
    unittest.main()


# python -m unittest testes.test_real