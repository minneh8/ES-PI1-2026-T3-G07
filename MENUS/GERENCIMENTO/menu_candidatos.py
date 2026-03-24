while True:
    try:
        print("\n1 - Edição de Dados\n2 - Cadastramento\n3 - Remoção \n4 - Busca de Candidatos \n5 - Candidatos")
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print("Edição de Dados")
            break    
        elif escolha == 2:
            print("Eleitores")
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")