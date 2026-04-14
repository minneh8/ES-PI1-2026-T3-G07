# Funções menu gerenciamento
import CondicoesGlobais as estado
def menu_gerenciamento_func():
    while estado.menu_principal == 1:
        try:
            print("\n0 - Voltar \n1 - Candidatos \n2 - Eleitores")
            estado.menu_gerenciamento = int(input("Escolha a opção desejada: "))
            match estado.menu_gerenciamento:
                case 0:
                    import menu_principal as main
                    print("Voltando...")
                    return (main.menu_principal_func())
                case 1:
                    print("Candidatos")
                    menu_candidatos_func()
                    break
                case 2:
                    print("Eleitores")
                    menu_eleitores_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Lista de candidatos"""
def menu_listacandidatos_func(): 
    while estado.menu_candidatos == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatos")
            estado.menu_listacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_listacandidatos:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                    print("Lista de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Lista de eleitores"""
def menu_listaeleitores_func():
    while estado.menu_eleitores == 1:
        try:
            print("\n0 - Voltar\n1 - Mostrar a lista de Eleitores")
            estado.menu_listaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_listaeleitores:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Mostrar a lista de Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Busca de candidatos"""
def menu_buscacandidatos_func():
    while estado.menu_candidatos == 3 : 
        try:
            print("\n0 - Voltar\n1 - Busca de Candidatos")
            estado.menu_buscacandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_buscacandidatos:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                    print("Busca de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


"""Remoção de candidatos"""
def menu_removecandidatos_func():
    while estado.menu_candidatos == 2:
        try:
            print("\n0 - Voltar\n1 - Remoção de Candidatos")
            estado.menu_removecandidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_removecandidatos:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                    print("Remoção de Candidatos")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Menu cadastro de candidatos"""
def menu_cadastramento_cand_func():
    while estado.menu_candidatos == 5:
        try:
            print("\n0 - Voltar\n1 - Cadastramento")
            estado.menu_cadastramento_cand= int(input("Escolha a opção desejada: "))
            match estado.menu_cadastramento_cand:
                case 0:
                    print("Voltando...")
                    menu_candidatos_func()
                    return
                case 1:
                    print("Cadastramento")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Menu Edição de dados - Candidatos"""
def menu_edicaodados_cand_func():
    while estado.menu_candidatos == 4:
        try:
            print("\n0 - Voltar \n1 - Editar Nome \n2 - Editar Idade \n3 - Editar Partido")
            estado.menu_edicaodados = int(input("Escolha a opção desejada: "))
            match estado.menu_edicaodados:
                case 0:
                    print("Voltando...")
                    return(menu_candidatos_func())
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

"""Menu Candidatos"""
def menu_candidatos_func():
    while estado.menu_gerenciamento == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatos \n2 - Remoção de Candidatos \n3 - Busca de Candidatos \n4 - Edição de Dados \n5 - Cadastramento")
            estado.menu_candidatos= int(input("Escolha a opção desejada: "))
            match estado.menu_candidatos:
                case 0:
                    print("Voltando...")
                    return(menu_gerenciamento_func())
                case 1:
                    print("Lista de Candidatos")
                    menu_listacandidatos_func()
                    break    
                case 2:
                    print("Remoção de Candidatos")
                    menu_removecandidatos_func()
                    break
                case 3 : 
                    print("Busca de Candidatos")
                    menu_buscacandidatos_func()
                    break   
                case 4: 
                    print("Edição de Dados")
                    menu_edicaodados_cand_func()
                    break
                case 5: 
                    print("Cadastramento")
                    menu_cadastramento_cand_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Busca Eleitores"""
def menu_buscaeleitores_func():
    while estado.menu_eleitores == 3:
        try:
            print("\n0 - Voltar\n1 - Buscar Eleitores")
            estado.menu_buscaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_buscaeleitores:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Buscar Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Cadastro Eleitores"""
def menu_cadastramento_ele_func():
    while estado.menu_eleitores == 5:
        try:
            print("\n0 - Voltar\n1 - Cadastramento de Eleitores")
            estado.menu_cadastramento_ele= int(input("Escolha a opção desejada: "))
            match estado.menu_cadastramento_ele:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Cadastramento de Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")    

"""Edição de dados - Eleitor"""
def menu_edicaodados_ele_func():
    while estado.menu_eleitores == 4:
        try:
            print("\n0 - Voltar\n1 - Editar Nome\n2 - Editar Idade\n3 - Editar Documentos")
            estado.menu_edicaodados_ele= int(input("Escolha a opção desejada: "))
            match estado.menu_edicaodados_ele:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Editar Nome")
                    break
                case 2:
                    print("Editar Idade")
                    break
                case 3: 
                    print("Editar Documentos")
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Remover eleitores"""
def menu_removeeleitores_func():
    while estado.menu_eleitores == 2:
        try:
            print("\n0 - Voltar\n1 - Remover Eleitores")
            estado.menu_removeeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_removeeleitores:
                case 0:
                    print("Voltando...")
                    menu_eleitores_func()
                    return
                case 1:
                    print("Remover Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Menu Eleitores"""
def menu_eleitores_func():
   
    while estado.menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores\n2 - Remoção de Eleitores \n3 - Busca de Eleitores \n4 - Edição de Dados \n5 - Cadastramento")
            estado.menu_eleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_eleitores:
                case 0:
                    print("Voltando...")
                    menu_gerenciamento_func()
                    return
                case 1:
                    print("Lista de Eleitores")
                    menu_listaeleitores_func()
                    break
                case 2:
                    print("Remoção de Eleitores")
                    menu_removeeleitores_func()
                    break
                case 3 : 
                    print("Busca de Eleitores")
                    menu_buscaeleitores_func()
                    break
                case 4: 
                    print("Edição de Dados")
                    menu_edicaodados_ele_func() 
                    break
                case 5: 
                    print("Cadastramento")
                    menu_cadastramento_ele_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
