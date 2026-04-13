import CondicoesGlobais as estado
import Menu_Candidatos as ct

def menu_buscacandidatos_func():
    while estado.menu_candidatos == 3 : 
        try:
            print("\n0 - Voltar\n1 - Busca de Candidatos")
            estado.menu_buscacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_buscacandidatos:
                case 0:
                    print("Voltando...")
                    ct.menu_candidatos_func()
                    return
                case 1:
                    print("Busca de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")