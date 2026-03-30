#import DATABASE
#conexao = DATABASE.conecta_mysql()
menu_principal = -1  
menu_gerenciamento = -1  
menu_votacao = -1  
menu_candidatos = -1
menu_eleitores = -1
menu_sistem_votacao = -1
menu_auditoria = -1
menu_resultado = -1
menu_edicaodados = -1
#Menu Principal
def menu_principal_func():  
    global menu_principal  
    while menu_principal != 0:
        try:
            print("\n0 - Encerrar \n1 - Gerenciamento \n2 - Votação")
            menu_principal = int(input("Escolha a opção desejada: "))
            match menu_principal:
                case 0:
                    print("Encerrando...")
                    break
                case 1:
                    print("Gerenciamento")
                    menu_gerenciamento_func()
                    break
                case 2:
                    print("Votação")
                    menu_votacao_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")
# Menu Gerenciamento 
def menu_gerenciamento_func():   
    global menu_gerenciamento 
    while menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Candidatos \n2 - Eleitores")
            menu_gerenciamento = int(input("Escolha a opção desejada: "))
            match menu_gerenciamento:
                case 0:
                    print("Voltando...")
                    return(menu_principal_func())
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
#Menu Votação
def menu_votacao_func():
    global menu_votacao
    while menu_principal == 2:
        try:
            print("0 - Voltar \n1 - Sistema de Votação \n2 - Auditoria \n3 - Resultado")
            menu_votacao= int(input("Escolha a opção desejada: "))
            match menu_votacao:
                case 0:
                    print("Voltando...")
                    return(menu_principal_func())
                case 1:
                    print("Sistema de Votação")
                    menu_sistem_votacao_func()
                    break
                case 2:
                    print("Auditoria")
                    menu_auditoria_func()
                    break
                case 3:
                    print("Resultado")
                    menu_resultado_func()
                    break
                case _:
                    print("Opção Invalida, tente novamente.")
        except ValueError:
            print("Entrada Inválida. Digite um Numero")
#Menu Candidatos
def menu_candidatos_func():
    global menu_candidatos
    while menu_gerenciamento == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatosn \n2 - Remoção de Candidatos \n3 - Busca de Candidatos \n4 - Edição de Dados \n5 - Cadastramento")
            menu_candidatos= int(input("Escolha a opção desejada: "))
            match menu_candidatos:
                case 0:
                    print("Voltando...")
                    return(menu_gerenciamento_func())
                case 1:
                    print("Lista de Candidatos")
                    break    
                case 2:
                    print("Remoção de Candidatos")
                    break
                case 3 : 
                    print("Busca de Candidatos")
                    break   
                case 4: 
                    print("Edição de Dados")
                    menu_edicaodados_func()
                    break
                case 5: 
                    print("Cadastramento")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
#Menu Eleitores
def menu_eleitores_func():
    global menu_eleitores
    while menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores\n2 - Remoção de Eleitores \n3 - Busca de Eleitores \n4 - Edição de Dados \n5 - Cadastramento")
            menu_eleitores= int(input("Escolha a opção desejada: "))
            match menu_eleitores:
                case 0:
                    print("Voltando...")
                    return(menu_gerenciamento_func())
                case 1:
                    print("Lista de Eleitores")
                    break    
                case 2:
                    print("Remoção de Eleitores")
                    break
                case 3 : 
                    print("Busca de Eleitores")
                    break   
                case 4: 
                    print("Edição de Dados")
                    break
                case 5: 
                    print("Cadastramento")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_sistem_votacao_func():
    global menu_sistem_votacao
    while menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Solicitar Dados")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            match menu_sistem_votacao:
                case 0:
                    print("Voltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Solitar Dados")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
def menu_auditoria_func():
    global menu_auditoria
    while menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Logs \n 2 - Protocolo de Votação")
            menu_auditoria= int(input("Escolha a opção desejada: "))
            match menu_auditoria:
                case 0:
                    print("Voltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Logs")
                    break   
                case 2:
                    print("Protocolo de Votação")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
def menu_resultado_func():
    global menu_resultado
    while menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna")
            menu_resultado= int(input("Escolha a opção desejada: "))
            match menu_resultado:
                case 0:
                    print("Voltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Boletim de Urna")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_para_votacao_func():
    global menu_para_votacao 
    while menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Votar \n2 - Encerrar Votação")
            menu_para_votacao = int(input("Escolha a opção desejada: "))
            match menu_para_votacao:
                case 0:
                    print("Voltando...")
                    return(menu_principal_func())
                case 1:
                    print("Votar")
                    menu_votacao_func()
                    break
                case 2:
                    print("Encerrar Votação")
                    confirmação=input("Tem certeza que deseja encerrar a votação? (s/n): ")
                    if confirmação.lower() == 's':
                        print("Votação encerrada.")
                    else: 
                        return(menu_para_votacao_func())
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")
def menu_edicaodados_func():
    global menu_edicaodados
    while menu_candidatos == 4:
        try:
            print("\n0 - Voltar \n1 - Editar Nome \n2 - Editar Idade \n3 - Editar Partido")
            menu_edicaodados = int(input("Escolha a opção desejada: "))
            match menu_edicaodados:
                case 0:
                    print("Voltando...")
                    return(menu_candidatos_func())
                case 1:
                    print("Editar Nome")
                    break
                case 2:
                    print("Editar Idade")
                    break
                case 3:
                    print("Editar Partido")
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")
menu_principal_func()