import unittest
from unittest.mock import patch
from modelos.profissionais import Profissional, adicionar_profissional, obter_profissional_por_nome, atualizar_profissional
from modelos.especialidades import Especialidade

class TestProfissionais(unittest.TestCase):

    def setUp(self):
        self.especialidadeCardiologia = Especialidade(id=1, nome="Cardiologia", descricao="Especialidade em Cardiologia")
        self.especialidadeNeurologia = Especialidade(id=3, nome="Neurologia", descricao="Especialidade em Neurologia")
        self.profissionalJoao = Profissional(id=1, nome="Dr. João Silva", cpf="123.456.789-00", contato="joao.silva@gmail.com", especialidade_id=1)
        self.profissionalMaria = Profissional(id=2, nome="Dra. Maria Oliveira", cpf="987.654.321-00", contato="maria.oliveira@gmail.com", especialidade_id=2)

    # Testa busca de profissional por nome
    @patch('modelos.profissionais.obter_profissional_por_nome')
    def test_obter_profissional_por_nome(self, mock_obter_profissional_por_nome):
        mock_obter_profissional_por_nome.return_value = self.profissionalJoao
        profissional = obter_profissional_por_nome("Dr. João Silva")
        self.assertIsNotNone(profissional)
        self.assertEqual(profissional.nome, "Dr. João Silva")
        self.assertEqual(profissional.cpf, "123.456.789-00")

    # Testa a atualização dos dados do profissional
    @patch('modelos.profissionais.atualizar_profissional')
    @patch('modelos.profissionais.obter_profissional_por_nome')
    def test_atualizar_profissional(self, mock_obter_profissional_por_nome, mock_atualizar_profissional):
        mock_obter_profissional_por_nome.return_value = self.profissionalJoao

        profissional = obter_profissional_por_nome("Dr. João Silva")
        self.assertIsNotNone(profissional)

        profissional.contato = "joao.silva@hotmail.com"
        atualizar_profissional(profissional)

        mock_obter_profissional_por_nome.return_value.contato = "joao.silva@hotmail.com"
        profissional_atualizado = obter_profissional_por_nome("Dr. João Silva")
        self.assertEqual(profissional_atualizado.contato, "joao.silva@hotmail.com")

    # Testa se o formato do CPF está no padrão esperado
    def test_formato_cpf(self):
        formatoCPF = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
        self.assertRegex(self.profissionalJoao.cpf, formatoCPF)
        self.assertRegex(self.profissionalMaria.cpf, formatoCPF)

    # Testa validação de CPF único
    @patch('modelos.profissionais.adicionar_profissional')
    @patch('modelos.profissionais.obter_profissional_por_nome')
    def test_validacao_cpf_unico(self, mock_obter_profissional_por_nome, mock_adicionar_profissional):
        mock_obter_profissional_por_nome.return_value = self.profissionalJoao
        profissional = Profissional(nome="Dr. Pedro Mendes", cpf="123.456.789-00", contato="pedro.mendes@gmail.com", especialidade_id=1)

        try:
            adicionar_profissional(profissional)
        except Exception as e:
            self.assertTrue("Duplicate entry" in str(e))

        mock_adicionar_profissional.assert_not_called()

    # Testa inserção de dados obrigatórios (nome, CPF, email)
    def test_insercao_dados_obrigatorios(self):
        # Testando nome em branco
        profissional_sem_nome = Profissional(nome="", cpf="656.555.666-77", contato="pedro.mendes@gmail.com", especialidade_id=1)
        with self.assertRaises(Exception):
            adicionar_profissional(profissional_sem_nome)

        # Testando CPF em branco
        profissional_sem_cpf = Profissional(nome="Dr. Pedro Mendes", cpf="", contato="pedro.mendes@gmail.com", especialidade_id=1)
        with self.assertRaises(Exception):
            adicionar_profissional(profissional_sem_cpf)

        # Testando email em branco
        profissional_sem_contato = Profissional(nome="Dr. Pedro Mendes", cpf="444.555.666-77", contato="", especialidade_id=1)
        with self.assertRaises(Exception):
            adicionar_profissional(profissional_sem_contato)

    # Testa formato de email
    def test_formato_email(self):
        # Testando email mal formatado
        profissional_email_invalido = Profissional(nome="Dr. Pedro Mendes", cpf="444.555.666-77", contato="email_invalido", especialidade_id=1)
        with self.assertRaises(Exception):
            adicionar_profissional(profissional_email_invalido)

if __name__ == "__main__":
    unittest.main()

# python -m unittest testes.test_simulado