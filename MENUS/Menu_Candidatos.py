"""Menu Candidatos"""
import CondicoesGlobais as estado
import Menu_Gerenciamento as gr
import Menu_EdicaoDados_Cand as ed
import Menu_ListaCandidatos as lc
import Menu_RemoveCandidatos as rc
import Menu_BuscaCandidatos as bc
import Menu_Cadastramento_Cand as cc
def menu_candidatos_func():
    
    while estado.menu_gerenciamento == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatosn \n2 - Remoção de Candidatos \n3 - Busca de Candidatos \n4 - Edição de Dados \n5 - Cadastramento")
            estado.menu_candidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_candidatos:
                case 0:
                    print("Voltando...")
                    return(gr.menu_gerenciamento_func())
                case 1:
                    print("Lista de Candidatos")
                    lc.menu_listacandidatos_func()
                    break    
                case 2:
                    print("Remoção de Candidatos")
                    rc.menu_removecandidatos_func()
                    break
                case 3 : 
                    print("Busca de Candidatos")
                    bc.menu_buscacandidatos_func()
                    break   
                case 4: 
                    print("Edição de Dados")
                    ed.menu_edicaodados_cand_func()
                    break
                case 5: 
                    print("Cadastramento")
                    cc.menu_cadastramento_cand_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")