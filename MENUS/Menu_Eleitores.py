"""Menu Eleitores"""
import CondicoesGlobais as estado

def menu_eleitores_func():
    import Menu_Gerenciamento as gr
    while estado.menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores\n2 - Remoção de Eleitores \n3 - Busca de Eleitores \n4 - Edição de Dados \n5 - Cadastramento")
            estado.menu_eleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_eleitores:
                case 0:
                    print("Voltando...")
                    gr.menu_gerenciamento_func()
                    return
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
