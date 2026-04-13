import CondicoesGlobais as estado
import Menu_Candidatos as ct

def menu_cadastramento_cand_func():
    while estado.menu_candidatos == 5:
        try:
            print("\n0 - Voltar\n1 - Cadastramento")
            estado.menu_cadastramento_cand= int(input("Escolha a opção desejada: "))
            match estado.menu_cadastramento_cand:
                case 0:
                    print("Voltando...")
                    ct.menu_candidatos_func()
                    return
                case 1:
                    print("Cadastramento")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")