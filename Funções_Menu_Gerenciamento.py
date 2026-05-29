# Funções menu gerenciamento
import CondicoesGlobais as estado
import DATABASE as db
import Validações as v
import Criptografia_hill_func as crypt
import numpy as np

def menu_gerenciamento_func():
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

"""Lista de candidatos"""
def menu_listacandidatos_func(): 
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
                    lista_candidatos()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Lista de eleitores"""
def menu_listaeleitores_func():
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

"""Busca de candidatos"""
def menu_buscacandidatos_func():
    while estado.menu_candidatos == 3 : 
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
                        busca_candidatos(termo)
                        break
                    
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


"""Remoção de candidatos"""

"""Menu cadastro de candidatos"""

"""Menu Edição de dados - Candidatos"""

"""Menu Candidatos"""
def menu_candidatos_func():
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
                    print("Busca de Candidatos")
                    menu_buscacandidatos_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Busca Eleitores"""
def menu_buscaeleitores_func():
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
                        db.conecta_mysql()
                        cursor = estado.connection.cursor(dictionary=True)  # Retorna dicionário em vez de tupla
    
                        query = "SELECT * FROM eleitores WHERE nome_ele LIKE %s"
                        cursor.execute(query, (f"%{termo}%",))
    
                        resultados = cursor.fetchall()
    
                        if not resultados:
                            print("Nenhum eleitor encontrado.")
                            return
    
                        for eleitor in resultados:
                            print(f"ID: {eleitor['id_ele']} | Nome: {eleitor['nome_ele']} | CPF: {eleitor['cpf_ele']} | Título Eleitoral: {eleitor['titulo_ele']}")
                        cursor.close()

                    busca_eleitores(termo)

                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Cadastro Eleitores"""
def menu_cadastramento_ele_func():
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

"""Menu Eleitores"""
def menu_eleitores_func():
   
    while estado.menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores \n2 - Busca de Eleitores \n3 - Cadastramento")
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
                    
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def cadastro_func():
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
            break
    except ValueError:
        print("CPF inválido.")


    estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
    v.validacao_tituloeleitor_func(estado.teleitor)
    try:
        while len(estado.teleitor) != 12 or estado.teleitorvalido == False:
            estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
            v.validacao_tituloeleitor_func(estado.teleitor)
            break
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


    estado.cadastro = "INSERT INTO eleitores (nome_ele, cpf_ele, titulo_ele, senha_ele, mesario_ele) VALUES (%s, %s, %s, %s, %s)"
    estado.valores = (estado.nome, cpfcripto, estado.teleitor, senhacripto, estado.mesario)
    estado.cursor.execute(estado.cadastro, estado.valores)
    estado.connection.commit()
    estado.cursor.close()
    estado.connection.close()
    print("Cadastro realizado com sucesso!")
    