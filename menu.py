while True:
    try:
        print("\n1 - Gerenciamento \n2 - Votação")
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print("Gerenciamento")
            break    
        elif escolha == 2:
            print("Votação")
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
