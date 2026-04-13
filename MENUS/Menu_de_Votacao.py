"""Para a Votação"""
import CondicoesGlobais as estado
def menu_para_votacao_func():
    import MENUS.menu_principal as main
    import Menu_Votacao as vt
    
    while estado.menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Votar \n2 - Encerrar Votação")
            estado.menu_para_votacao = int(input("Escolha a opção desejada: "))
            match estado.menu_para_votacao:
                case 0:
                    print("Voltando...")
                    return(main.menu_principal_func())
                case 1:
                    print("Votar")
                    vt.menu_votacao_func()
                    break
                case 2:
                    print("Encerrar Votação")
                    confirmação=input("Tem certeza que deseja encerrar a votação? (s/n): ")
                    if confirmação.lower() == 's':
                        print("Votação encerrada.")
                    else: 
                        return(menu_para_votacao_func())
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")