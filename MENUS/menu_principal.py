#import DATABASE
#conexao = DATABASE.conecta_mysql()

"""Menu Principal"""
import CondicoesGlobais as estado

def menu_principal_func():  
    import Menu_Gerenciamento as gr
    import Menu_Votacao as vt

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
                    print("Votação")
                    vt.menu_votacao_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")

menu_principal_func()