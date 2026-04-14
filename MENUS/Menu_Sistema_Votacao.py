"""Sitema de Votação"""
import CondicoesGlobais as estado
import Menu_Votacao as vt
def menu_sistem_votacao_func():
    
    while estado.menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Comecar Votação\n2 - Fechar Sistema de Votação")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            match menu_sistem_votacao:
                case 0:
                    print("\nVoltando...")
                    return(vt.menu_votacao_func())
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