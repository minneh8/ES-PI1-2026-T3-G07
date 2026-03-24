while True:
    try:
        print("\n1 - Gerenciamento \n2 - Votação")
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print("Gerenciamento")
            while True:
                try:
                    print("\n1 - Candidatos \n2 - Eleitores")
                    escolha = int(input("Escolha a opção desejada: "))
                    if escolha == 1:
                        print("Candidatos")
                        while True:
                            try:
                                print("\n1 - Edição de Dados\n2 - Cadastramento\n3 - Remoção \n4 - Busca de Candidatos \n5 - Candidatos \n0 - Voltar")
                                escolha = int(input("Escolha a opção desejada: "))
                                if escolha == 0 :
                                    
                                    print("Voltando..." )
                                elif escolha == 1:
                                    print("Edição de Dados")
                                    break    
                                elif escolha == 2:
                                    print("Eleitores")
                                    break
                                    print("Opção inválida, tente novamente.")
                            except ValueError:
                                print("Entrada inválida. Digite um número.")
                    elif escolha == 2:
                        print("Eleitores")
                        break
                    else:
                        print("Opção inválida, tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")   
        elif escolha == 2:
            print("Votação")
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

