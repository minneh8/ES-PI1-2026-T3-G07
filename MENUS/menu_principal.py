#import DATABASE
#conexao = DATABASE.conecta_mysql()
"""Menu Principal"""
import CondicoesGlobais as estado
import Funções_Menu_Gerenciamento as gr
import Funções_Menu_Votação as vt

def menu_principal_func(): 
    while estado.menu_principal != 0:
        try:
            print("\n0 - Encerrar \n1 - Gerenciamento \n2 - Votação")
            estado.menu_principal = int(input("Escolha a opção desejada: "))

            match estado.menu_principal:
                case 0:
                    print("Encerrando...")
                    break
                case 1:
                    print("Gerenciamento")
                    gr.menu_gerenciamento_func()
                    break
                case 2:
                    print("\n Votação")
                    vt.menu_votacao_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")

menu_principal_func()