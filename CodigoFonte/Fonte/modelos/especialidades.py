import mysql.connector

# Configuração do banco de dados MySQL
db_config = {
    "host": "localhost",
    "user": "",
    "password": "",
    "database": "sistema_profissionais",
}

class Especialidade:
    def __init__(self, id=None, nome=None, descricao=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

def adicionar_especialidade(especialidade):
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Cria uma transação com a query INSERT com dados vindos do form
        cursor.execute("INSERT INTO ESPECIALIDADE (nome, descricao) VALUES (%s, %s)", (especialidade.nome, especialidade.descricao))
        # Executa efetivamente a query
        conn.commit()
        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
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
