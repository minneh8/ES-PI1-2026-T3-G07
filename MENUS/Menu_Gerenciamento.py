"""Menu Gerenciamento"""
import CondicoesGlobais as estado
def menu_gerenciamento_func():
    import menu_principal as main
    import Menu_Candidatos as ct
    import Menu_Eleitores as el

    while estado.menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Candidatos \n2 - Eleitores")
            estado.menu_gerenciamento = int(input("Escolha a opção desejada: "))
            match estado.menu_gerenciamento:
                case 0:
                    print("Voltando...")
                    main.menu_principal_func()
                    return
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