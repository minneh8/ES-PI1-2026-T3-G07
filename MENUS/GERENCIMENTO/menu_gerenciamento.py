while True:
    try:
        print("\n1 - Candidatos \n2 - Eleitores")
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print("Candidatos")
            break    
        elif escolha == 2:
            print("Eleitores")
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")