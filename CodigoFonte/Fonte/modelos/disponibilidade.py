import mysql.connector

# Configuração do banco de dados MySQL
db_config = {
    "host": "localhost",
    "user": "",
    "password": "",
    "database": "sistema_profissionais",
}

class Disponibilidade:
    def __init__(self, profissional_id, dia_semana, horario_inicio, horario_fim):
        self.profissional_id = profissional_id
        self.dia_semana = dia_semana
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim

def obter_disponibilidade(nome=None, especialidade=None):
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        SELECT p.nome, e.nome AS especialidade, d.dia_semana, d.horario_inicio, d.horario_fim
        FROM DISPONIBILIDADE d
        JOIN PROFISSIONAL p ON d.profissional_id = p.id
        JOIN ESPECIALIDADE e ON p.especialidade_id = e.id
        """

        atributos = []
        condicao = []
        if nome:
            condicao.append("p.nome LIKE %s")
            atributos.append(f"%{nome}%")
        if especialidade:
            condicao.append("e.nome LIKE %s")
            atributos.append(f"%{especialidade}%")

        if condicao:
            query += " WHERE " + " AND ".join(condicao)

        cursor.execute(query, atributos)
        resultados = cursor.fetchall()

        # Fechando o cursor e a conexão
        cursor.close()
        conn.close()

        return resultados
    
    except mysql.connector.Error as err:
        raise Exception(f"Erro do MySQL: {str(err)} - SQLSTATE: {err.sqlstate}")
    except Exception as e:
        raise Exception(f"Erro desconhecido: {str(e)}")