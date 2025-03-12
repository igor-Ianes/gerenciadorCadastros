import mysql.connector
import re

# Configuração do banco de dados MySQL
db_config = {
    "host": "localhost",
    "user": "",
    "password": "",
    "database": "sistema_profissionais",
}

class Profissional:
    def __init__(self, id=None, nome=None, cpf=None, contato=None, especialidade_id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.especialidade_id = especialidade_id

class Especialidade:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

def adicionar_profissional(profissional):
    # Validação do CPF
    cpf_pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if not re.match(cpf_pattern, profissional.cpf):
        raise Exception("O CPF informado não obedece ao formato XXX.XXX.XXX-XX")

    # Validação do Email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, profissional.contato):
        raise Exception("O E-MAIL informado não obedece ao formato XXX@XXXX.XX")

    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Cria uma transação com a query INSERT com dados vindos do form
        cursor.execute("INSERT INTO PROFISSIONAL (nome, cpf, contato, especialidade_id) VALUES (%s, %s, %s, %s)",
                       (profissional.nome, profissional.cpf, profissional.contato, profissional.especialidade_id))
        # Executa efetivamente a query
        conn.commit()

        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")

def obter_profissionais():
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Busca dados no banco de dados atraves do comando se consulta SELECT
        cursor.execute("SELECT id, nome FROM PROFISSIONAL")
        profissionais = cursor.fetchall()

        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()

        return [Profissional(id=id, nome=nome) for id, nome in profissionais]
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")

def obter_profissional_por_nome(nome):
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Busca dados no banco de dados atraves do comando se consulta SELECT
        cursor.execute("SELECT id, nome, cpf, contato, especialidade_id FROM PROFISSIONAL WHERE nome = %s", (nome,))
        profissional = cursor.fetchone()

        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()

        if profissional:
            return Profissional(*profissional)
        return None
    
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")

def atualizar_profissional(profissional):
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Atualizando dados no banco de dados atraves do comando UPDATE
        cursor.execute("UPDATE PROFISSIONAL SET cpf = %s, contato = %s, especialidade_id = %s WHERE id = %s",
                       (profissional.cpf, profissional.contato, profissional.especialidade_id, profissional.id))
        # Executa efetivamente a query
        conn.commit()

        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate} <br><br> O CPF informado não obedece ao formato XXX.XXX.XXX-XX<br>")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")

def obter_especialidades_por_nome(nome=None):
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "SELECT id, nome FROM ESPECIALIDADE"
        if nome:
            query += " WHERE nome = %s"
            cursor.execute(query, (nome,))
        else:
            cursor.execute(query)

        especialidades = cursor.fetchall()

        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()

        return [Especialidade(id=id, nome=nome) for id, nome in especialidades]
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")
