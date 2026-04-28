import CondicoesGlobais as estado
def conecta_mysql():    
    import mysql.connector
    from mysql.connector import Error

    try:
        # Establish the connection
        estado.connection = mysql.connector.connect(
            host='127.0.0.1',          # or the IP address of your MySQL server
            port=3306,                 # default port
            user='root',      # your MySQL username
            password='Curintia80@',  # your MySQL password
            database='Projeto_Integrador_1'   # the specific database you want to use
        )
        if estado.connection.is_connected():
            estado.cursor = estado.connection.cursor()

            
    except Error as e:
        print(f"Erro ao conectar to MySQL: {e}")
    except mysql.connector.Error as erro:
        print(f"Erro na insercao no MySQL: {erro}")
