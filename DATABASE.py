"""
Módulo de Banco de Dados.

Responsável por estabelecer e disponibilizar a conexão com o banco
de dados MySQL utilizado pelo sistema eleitoral. A conexão criada é
armazenada nas variáveis globais do sistema, permitindo que os demais
módulos realizem consultas, inserções, atualizações e remoções de
dados relacionados a eleitores, candidatos, votos, partidos e logs.
"""

import CondicoesGlobais as estado
def conecta_mysql():    
    """
    Estabelece conexão com o banco de dados MySQL.

    A função realiza a conexão com o banco de dados do sistema
    eleitoral utilizando as credenciais configuradas e armazena
    os objetos de conexão e cursor nas variáveis globais do sistema.

    Returns:
        None

    Args:
        None
    """
    import mysql.connector
    from mysql.connector import Error

    try:
        # Establish the connection
        estado.connection = mysql.connector.connect(
            host='127.0.0.1',         
            port=3306,                 
            user='root',      
            password='Mogato@123',  
            database='sistema_votacao'   
        )
        if estado.connection.is_connected():
            estado.cursor = estado.connection.cursor()

            
    except Error as e:
        print(f"Erro ao conectar to MySQL: {e}")
    except mysql.connector.Error as erro:
        print(f"Erro na insercao no MySQL: {erro}")
