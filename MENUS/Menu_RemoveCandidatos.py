import CondicoesGlobais as estado
import Menu_Candidatos as ct

def menu_removecandidatos_func():
    while estado.menu_candidatos == 2:
        try:
            print("\n0 - Voltar\n1 - Remoção de Candidatos")
            estado.menu_removecandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_removecandidatos:
                case 0:
                    print("Voltando...")
                    ct.menu_candidatos_func()
                    return
                case 1:
                    print("Remoção de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")