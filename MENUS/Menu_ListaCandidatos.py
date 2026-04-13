import CondicoesGlobais as estado
import Menu_Candidatos as ct

def menu_listacandidatos_func(): 
    while estado.menu_candidatos == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatos")
            estado.menu_listacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_listacandidatos:
                case 0:
                    print("Voltando...")
                    ct.menu_candidatos_func()
                    return
                case 1:
                    print("Lista de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")