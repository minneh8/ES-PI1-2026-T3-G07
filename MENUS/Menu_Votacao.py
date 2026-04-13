"""Menu Votação"""
import CondicoesGlobais as estado
import Menu_Auditoria as meau
import Menu_Sistema_Votacao as mesv
import Menu_Resultado as mer

def menu_votacao_func():
    while estado.menu_principal == 2:
        try:
            print("0 - Voltar \n1 - Sistema de Votação \n2 - Auditoria \n3 - Resultado")
            estado.menu_votacao= int(input("Escolha a opção desejada: "))
            match estado.menu_votacao:
                case 0:
                    import MENUS.menu_principal as main
                    print("\n Voltando... ")
                    main.menu_principal_func()
                    return
                case 1:
                    print("Sistema de Votação")
                    mesv.menu_sistem_votacao_func()
                    break
                case 2:
                    print("Auditoria")
                    meau.menu_auditoria_func()
                    break
                case 3:
                    print("Resultado")
                    mer.menu_resultado_func()
                    break
                case _:
                    print("Opção Invalida, tente novamente.")
        except ValueError:
            print("Entrada Inválida. Digite um Numero")