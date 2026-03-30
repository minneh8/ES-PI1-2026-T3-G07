def conecta_mysql():    
    import mysql.connector
    from mysql.connector import Error

    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='127.0.0.1',          # or the IP address of your MySQL server
            port=3306,                 # default port
            user='root',      # your MySQL username
            password='Curintia80@',  # your MySQL password
            database='Projeto_Integrador_1'   # the specific database you want to use
        )
        if connection.is_connected():
            cursor = connection.cursor()
            print("Você esta conectado ao banco de dados com sucesso!")


    except Error as e:
        print(f"Erro ao conectar to MySQL: {e}")

