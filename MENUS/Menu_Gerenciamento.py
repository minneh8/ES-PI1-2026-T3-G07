"""Menu Gerenciamento"""
import CondicoesGlobais as estado
import Menu_Candidatos as ct
import Menu_Eleitores as el
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
                    ct.menu_candidatos_func()
                    break
                case 2:
                    print("Eleitores")
                    el.menu_eleitores_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")