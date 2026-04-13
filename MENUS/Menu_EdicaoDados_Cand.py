"""Edição de Dados"""
import CondicoesGlobais as estado
import Menu_Candidatos as ct

def menu_edicaodados_cand_func():
    while estado.menu_candidatos == 4:
        try:
            print("\n0 - Voltar \n1 - Editar Nome \n2 - Editar Idade \n3 - Editar Partido")
            estado.menu_edicaodados = int(input("Escolha a opção desejada: "))
            match estado.menu_edicaodados:
                case 0:
                    print("Voltando...")
                    return(ct.menu_candidatos_func())
                case 1:
                    print("Editar Nome")
                    break
                case 2:
                    print("Editar Idade")
                    break
                case 3:
                    print("Editar Partido")
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")