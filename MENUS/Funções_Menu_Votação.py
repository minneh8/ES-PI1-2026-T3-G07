#Funções menus Votação
import CondicoesGlobais as estado

"""Menu Votação"""
def menu_votacao_func():
    while estado.menu_principal == 2:
        try:
            print("0 - Voltar \n1 -  Abrir Sistema de Votação \n2 - Auditoria \n3 - Resultado")
            estado.menu_votacao= int(input("Escolha a opção desejada: "))
            match estado.menu_votacao:
                case 0:
                    import menu_principal as main
                    print("\n Voltando... ")
                    return(main.menu_principal_func())
                case 1:
                    print(" Abrir Sistema de Votação")
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


"""Auditoria"""
def menu_auditoria_func():
    while estado.menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Logs \n2 - Protocolo de Votação")
            estado.menu_auditoria= int(input("Escolha a opção desejada: "))
            match estado.menu_auditoria:
                case 0:
                    print("\nVoltando...")
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

"""Sistema De Votação"""
def menu_sistem_votacao_func():
    
    while estado.menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Comecar Votação\n2 - Fechar Sistema de Votação")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            match menu_sistem_votacao:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Comecar Votação")
                    break
                case 2:
                    print("Encerrando Sistema de Votação...")
                    import menu_principal as main
                    return(main.menu_principal_func())
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

""""Menu Resultado"""
def menu_resultado_func():

    while estado.menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna")
            estado.menu_resultado= int(input("Escolha a opção desejada: "))
            match estado.menu_resultado:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Boletim de Urna")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

