"""
Módulo de Gerenciamento.

Responsável pelas funcionalidades administrativas do sistema
eleitoral, incluindo gerenciamento de candidatos e eleitores,
consultas ao banco de dados, buscas, listagens e cadastramento
de novos eleitores.

O módulo também realiza a integração com o banco de dados MySQL,
validações de documentos e rotinas de criptografia utilizadas
durante o processo de cadastro.
"""

import CondicoesGlobais as estado
import DATABASE as db
import Validações as v
import Criptografia_hill_func as crypt
import Descriptografia_hill_func as decrypt
import numpy as np

def menu_gerenciamento_func():

    """
    Exibe o menu de gerenciamento do sistema.

    Permite ao usuário acessar as funcionalidades relacionadas
    ao gerenciamento de candidatos e eleitores.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Candidatos \n2 - Eleitores")
            estado.menu_gerenciamento = int(input("Escolha a opção desejada: "))
            match estado.menu_gerenciamento:
                case 0:
                    import menu_principal as main
                    print("Voltando...")
                    return (main.menu_principal_func())
                case 1:
                    print("Candidatos")
                    menu_candidatos_func()
                    break
                case 2:
                    print("Eleitores")
                    menu_eleitores_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_listacandidatos_func(): 

    """
    Exibe o menu de listagem de candidatos.

    Permite visualizar todos os candidatos cadastrados
    no sistema.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_candidatos == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatos")
            estado.menu_listacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_listacandidatos:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                    def lista_candidatos():
                            db.conecta_mysql()
                            cursor = estado.connection.cursor(dictionary=True)  # Retorna dicionário em vez de tupla
        
                            query = "SELECT * FROM candidatos "
                            cursor.execute(query)
        
                            resultados = cursor.fetchall()
        
                            if not resultados:
                                print("Nenhum eleitor encontrado.")
                                return
        
                            for candidato in resultados:
                                print(f"Numero eleitoral: {candidato['num']} | Nome: {candidato['nome']} | Numero do Partido: {candidato['id_part']}\n")
                            cursor.close()
                            return
                    
                    lista_candidatos()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_listaeleitores_func():

    """
    Exibe o menu de listagem de eleitores.

    Permite visualizar todos os eleitores cadastrados
    no sistema.
    
    Args:
        None

    Returns:
        None
    """

    while estado.menu_eleitores == 1:
        try:
            print("\n0 - Voltar\n1 - Mostrar a lista de Eleitores")
            estado.menu_listaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_listaeleitores:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Mostrando a lista de Eleitores...")
                    def listaeleitores():
                        db.conecta_mysql()
                        cursor = estado.connection.cursor(dictionary=True)  # Retorna dicionário em vez de tupla
    
                        query = "SELECT * FROM eleitores "
                        cursor.execute(query)
    
                        resultados = cursor.fetchall()
    
                        if not resultados:
                            print("Nenhum eleitor encontrado.")
                            return
    
                        for eleitor in resultados:
                            print(f" Nome: {eleitor['nome_ele']} | Título Eleitoral: {eleitor['titulo_ele']}\n")
                        cursor.close()
                    listaeleitores()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_buscacandidatos_func():

    """
    Exibe o menu de busca de candidatos.

    Permite pesquisar candidatos cadastrados por nome.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_candidatos == 2 : 
        try:
            print("\n0 - Voltar\n1 - Busca de Candidatos")
            estado.menu_buscacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_buscacandidatos:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                        termo = input("Digite o nome para buscar: ")
                        def busca_candidatos(termo):

                            """
                            Busca candidatos no sistema pelo nome.

                            A função realiza uma busca no banco de dados por candidatos
                            cujo nome contenha o termo informado. Os resultados são exibidos
                            com número eleitoral, nome e número do partido.

                            Args:
                                termo (str): Termo de busca para filtrar candidatos pelo nome.
                                            A busca é parcial (LIKE %termo%).

                            Returns:
                                None. Exibe os resultados encontrados no console ou mensagem
                                informando que nenhum candidato foi encontrado.
                            """

                            db.conecta_mysql()
                            cursor = estado.connection.cursor(dictionary=True)  # Retorna dicionário em vez de tupla
        
                            query = "SELECT * FROM candidatos WHERE nome LIKE %s"
                            cursor.execute(query, (f"%{termo}%",))
        
                            resultados = cursor.fetchall()
        
                            if not resultados:
                                print("Nenhum eleitor encontrado.")
                                return
                            

                            for candidato in resultados:
                                print(f"Numero eleitoral: {candidato['num']} | Nome: {candidato['nome']} | Numero do Partido: {candidato['id_part']}")
                            cursor.close()
                            return
                        busca_candidatos(termo)
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_candidatos_func():
    
    """
    Exibe o menu de candidatos.

    Permite acessar funcionalidades de consulta,
    busca e gerenciamento de candidatos.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_gerenciamento == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatos \n2 - Busca de Candidatos \n")
            estado.menu_candidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_candidatos:
                case 0:
                    print("Voltando...")
                    return(menu_gerenciamento_func())
                case 1:
                    print("Lista de Candidatos")
                    menu_listacandidatos_func()
                    break    
                case 2:
                    menu_buscacandidatos_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_buscaeleitores_func():

    """
    Exibe o menu de busca de eleitores.

    Permite pesquisar eleitores cadastrados por nome.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_eleitores == 2:
        try:
            print("\n0 - Voltar\n1 - Buscar Eleitores")
            estado.menu_buscaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_buscaeleitores:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Buscar Eleitores")
                    termo = input("Digite o nome para buscar: ")
                    def busca_eleitores(termo):

                        """
                        Busca eleitores no sistema pelo nome.

                        A função realiza uma busca no banco de dados por eleitores
                        cujo nome contenha o termo informado. Os resultados são exibidos
                        com ID, nome, CPF (descriptografado) e título eleitoral.

                        Args:
                            termo (str): Termo de busca para filtrar eleitores pelo nome.
                                        A busca é parcial (LIKE %termo%).

                        Returns:
                            None. Exibe os resultados encontrados no console ou mensagem
                            informando que nenhum eleitor foi encontrado.

                        Nota:
                            O CPF é automaticamente descriptografado usando a Cifra de Hill
                            antes de ser exibido, garantindo que não seja mostrado criptografado.
                        """

                        db.conecta_mysql()
                        cursor = estado.connection.cursor(dictionary=True)  # Retorna dicionário em vez de tupla
    
                        query = "SELECT * FROM eleitores WHERE nome_ele LIKE %s"
                        cursor.execute(query, (f"%{termo}%",))
    
                        resultados = cursor.fetchall()
    
                        if not resultados:
                            print("Nenhum eleitor encontrado.")
                            return
                        matriz_inversa = [[1, -1], [0, 1]]
                        for eleitor in resultados:
                            cpf_descriptografado = decrypt.decifra_hill(eleitor['cpf_ele'], matriz_inversa)
                            print(f"ID: {eleitor['id_ele']} | Nome: {eleitor['nome_ele']} | CPF: {(cpf_descriptografado[:11])} | Título Eleitoral: {eleitor['titulo_ele']}")
                        cursor.close()

                    busca_eleitores(termo)

                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_cadastramento_ele_func():

    """
    Exibe o menu de cadastramento de eleitores.

    Permite iniciar o processo de cadastro de um
    novo eleitor no sistema.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_eleitores == 3:
        try:
            print("\n0 - Voltar\n1 - Cadastramento de Eleitores")
            estado.menu_cadastramento_ele= int(input("Escolha a opção desejada: "))
            match estado.menu_cadastramento_ele:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Cadastramento de Eleitores") 
                    cadastro_func()
                    print("\nVoltando...")
                    import menu_principal as main
                    return (main.menu_principal_func())
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")    

def edicao_dados():
    """
    Permite editar os dados de um eleitor cadastrado.

    A função localiza o eleitor através do título eleitoral,
    exibe os dados atuais descriptografados e permite a
    alteração das informações desejadas. Após a edição,
    os dados são criptografados novamente e atualizados
    no banco de dados.

    Args:
        None

    Returns:
        None
    """

    db.conecta_mysql()
    try:
        titulo = input("Digite o título eleitoral do eleitor: ")

        query = """
        SELECT nome_ele, titulo_ele, cpf_ele, mesario_ele, senha_ele
        FROM eleitores
        WHERE titulo_ele = %s
        """

        estado.cursor.execute(query, (titulo,))
        eleitor = estado.cursor.fetchone()

        if eleitor is None:
            print("Eleitor não encontrado.")
            return

        matriz_inversa = [[1, -1], [0, 1]]

        nome_atual = eleitor[0]
        titulo_atual = eleitor[1]
        cpf_atual = decrypt.decifra_hill(eleitor[2], matriz_inversa)
        mesario_atual = "SIM" if eleitor[3] == 1 else "NÃO"
        senha_atual = decrypt.decifra_hill(eleitor[4], matriz_inversa)

        print("\n===== DADOS ATUAIS =====")
        print(f"Nome: {nome_atual}")
        print(f"CPF: {cpf_atual}")
        print(f"Título: {titulo_atual}")
        print(f"Mesário: {mesario_atual}")
        print(f"Senha: {senha_atual}")

        print("\n===== NOVOS DADOS =====")
        novo_cpf = input(f"Novo CPF [{cpf_atual}]: ").strip() or cpf_atual
        if novo_cpf != cpf_atual:  # Só valida se mudou
            while len(novo_cpf) != 11:
                print("CPF deve conter 11 dígitos!")
                novo_cpf = input(f"Novo CPF [{cpf_atual}]: ").strip() or cpf_atual
            
            estado.cpf = novo_cpf
            v.validacao_cpf_func(novo_cpf)
            while not estado.cpfvalido:
                novo_cpf = input(f"Novo CPF [{cpf_atual}]: ").strip() or cpf_atual
                estado.cpf = novo_cpf
                v.validacao_cpf_func(novo_cpf)

        novo_titulo = input(f"Novo título [{titulo_atual}]: ").strip() or titulo_atual
        if novo_titulo != titulo_atual:  # Só valida se mudou
            while len(novo_titulo) != 12:
                print("Título deve conter 12 dígitos!")
                novo_titulo = input(f"Novo título [{titulo_atual}]: ").strip() or titulo_atual
            
            estado.teleitor = novo_titulo
            v.validacao_tituloeleitor_func(novo_titulo)
            while not estado.teleitorvalido:
                novo_titulo = input(f"Novo título [{titulo_atual}]: ").strip() or titulo_atual
                estado.teleitor = novo_titulo
                v.validacao_tituloeleitor_func(novo_titulo)

        novo_nome = input(f"Novo nome [{nome_atual}]: ").strip() or nome_atual
        novo_mesario = input(f"Mesário (S/N) [{mesario_atual}]: ").strip().upper()

        if novo_mesario == "":
            novo_mesario = eleitor[3]
        else:
            novo_mesario = 1 if novo_mesario == "S" else 0

        estado.nome = novo_nome
        v.gerador_senha_func()
        print(f"\nNova senha gerada: {estado.senha}")

        matriz = [[1, 1], [0, 1]]
        cpf_cripto = crypt.cifra_hill(novo_cpf, matriz)
        senha_cripto = crypt.cifra_hill(estado.senha, matriz)
        db.conecta_mysql()
        query_update = """
        UPDATE eleitores
        SET nome_ele = %s,
            titulo_ele = %s,
            cpf_ele = %s,
            mesario_ele = %s,
            senha_ele = %s
        WHERE titulo_ele = %s
        """

        estado.cursor.execute(
            query_update,
            (novo_nome, novo_titulo, cpf_cripto, novo_mesario, senha_cripto, titulo)
        )

        estado.connection.commit()
        print("\nDados atualizados com sucesso!")

    except Exception as erro:
        print(f"Erro ao editar eleitor: {erro}")
    finally:
        estado.cursor.close()
        estado.connection.close()

def menu_eleitores_func():

    """
    Exibe o menu de eleitores.

    Permite acessar funcionalidades relacionadas à
    consulta, busca e cadastramento de eleitores.

    Args:
        None

    Returns:
        None
    """   

    while estado.menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores \n2 - Busca de Eleitores \n3 - Cadastramento \n4 - Edição de dados")
            estado.menu_eleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_eleitores:
                case 0:
                    print("Voltando...")
                    menu_gerenciamento_func()
                    return
                case 1:
                    print("Lista de Eleitores")
                    menu_listaeleitores_func()
                    
                case 2 : 
                    print("Busca de Eleitores")
                    menu_buscaeleitores_func()
                case 3: 
                    print("Cadastramento")
                    menu_cadastramento_ele_func()
                case 4:
                    print("Edição de dados")
                    edicao_dados()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def cadastro_func():

    """
    Realiza o cadastro de um novo eleitor.

    A função solicita os dados do eleitor, valida CPF
    e título eleitoral, gera uma senha automática,
    criptografa informações sensíveis utilizando a
    Cifra de Hill e registra o eleitor no banco de dados.

    Args:
        None

    Returns:
        None
    """

    db.conecta_mysql()
    print("Para realizar o cadastro, por favor, digite o seu Nome, Sobrenome, CPF, Titulo Eleitoral.\nSua Senha será gerada automaticamente.\n")
    estado.nome = str(input("Digite o seu Nome Completo: "))
    try:
        while len(estado.nome) < 3:
            print("Nome inválido. O nome deve conter pelo menos 3 caracteres.")
            estado.nome = str(input("Digite o seu Nome Completo: "))
    except ValueError:
        print("Nome inválido. O nome deve conter pelo menos 3 caracteres.")


    estado.cpf = input("Digite o seu CPF: ")
    try:
        v.validacao_cpf_func(estado.cpf)
        while len(estado.cpf) != 11 or estado.cpfvalido == False:
            estado.cpf = input("Digite o seu CPF: ")
            v.validacao_cpf_func(estado.cpf)
    except ValueError:
        print("CPF inválido.")


    estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
    v.validacao_tituloeleitor_func(estado.teleitor)
    try:
        while len(estado.teleitor) != 12 or estado.teleitorvalido == False:
            estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
            v.validacao_tituloeleitor_func(estado.teleitor)
    except ValueError:
        print("Titulo Eleitor inválido.")
    estado.mesario = input("Você quer ser mesario? (S/N): ").upper()
    if estado.mesario == "S":
        estado.mesario = True
    else:
        estado.mesario = False
    v.gerador_senha_func()
    print(f"Sua senha gerada foi: {estado.senha}")
    np.matriz = [
        [1, 1],
        [0, 1]
    ]

    cpfcripto = crypt.cifra_hill(estado.cpf, np.matriz)

    senhacripto = crypt.cifra_hill(estado.senha, np.matriz)

    db.conecta_mysql()
    estado.cadastro = "INSERT INTO eleitores (nome_ele, titulo_ele, cpf_ele, mesario_ele, senha_ele) VALUES (%s, %s, %s, %s, %s)"
    estado.valores = (estado.nome, estado.teleitor, cpfcripto,estado.mesario, senhacripto)
    estado.cursor.execute(estado.cadastro, estado.valores)
    estado.connection.commit()
    estado.cursor.close()
    estado.connection.close()
    print("Cadastro realizado com sucesso!")