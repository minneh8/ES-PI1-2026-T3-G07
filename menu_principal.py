"""
Módulo Menu Principal.

Responsável por exibir o menu principal do sistema
e direcionar o usuário para as funcionalidades
disponíveis.
"""

import CondicoesGlobais as estado
import Funções_Menu_Gerenciamento as gr
import Funções_Menu_Votação as vt

def menu_principal_func(): 

    """
    Exibe e controla o menu principal do sistema eleitoral.

    Permite ao usuário acessar os módulos de Gerenciamento,
    Votação ou encerrar a execução do sistema.

    Args:
        None

    Returns:
        None: A função apenas direciona o fluxo do programa
        para o menu selecionado pelo usuário.
    """

    while estado.menu_principal != 0:
        try:
            print("\n0 - Encerrar \n1 - Gerenciamento \n2 - Votação")
            estado.menu_principal = int(input("Escolha a opção desejada: "))

            match estado.menu_principal:
                case 0:
                    print("Encerrando...")
                    break
                case 1:
                    print("Gerenciamento")
                    gr.menu_gerenciamento_func()
                    break
                case 2:
                    print("\n Votação")
                    vt.menu_votacao_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")    
        except ValueError:
            print("Entrada inválida. Digite um número.")

menu_principal_func()