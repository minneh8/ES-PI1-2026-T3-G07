"""Auditoria"""
import CondicoesGlobais as estado
import Menu_Votacao
def menu_auditoria_func():
    while estado.menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Logs \n2 - Protocolo de Votação")
            estado.menu_auditoria= int(input("Escolha a opção desejada: "))
            match estado.menu_auditoria:
                case 0:
                    print("Voltando...")
                    return(Menu_Votacao.menu_votacao_func())
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

menu_auditoria_func()