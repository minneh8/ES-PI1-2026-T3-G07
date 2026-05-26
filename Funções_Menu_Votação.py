#Funções menus Votação
import CondicoesGlobais as estado
from datetime import datetime
import DATABASE as db
import Validações as v

#Resgistrando o LOG de votação
def registrar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo: #Abrir arquivo logs.txt na UTF-8
        datahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #Usando o import para salvar a data certa do computador convertendo em strings (STRF)
        arquivo.write(f"[{datahora}] {mensagem}\n") #Escrevendo no arquivo


#Funcão para realizar votação, onde o usuário digita o número do candidato e o voto é registrado
def realizar_votacao_func():
        db.conecta_mysql()
        #Verificar se o sistema está aberto
        if estado.sistema_votacao_aberto == False:
            print("\nSistema de votação fechado! Você não pode votar agora.")
            return
        try:            #mostrando os candidatos usando FOR
            print("\n===== VOTAÇÃO =====")

            voto = input("Digite o número do candidato: ")               

            #Verificando se o candidato existe
            #Query para selecionar todos os candidatos do MySQL via número
            query_validacao = """
            SELECT * FROM candidatos
            WHERE num = %s
            """
            confirmar_voto = input("\nConfirma o voto? (S/N): ")
            if confirmar_voto.upper() != "S":
                print("Voto cancelado!")
                return
            
            estado.cursor.execute(query_validacao, (voto,))

            #salvando em uma variável
            candidato_existe = estado.cursor.fetchone()

            if candidato_existe == None:
                print("Candidato não encontrado!")
                registrar_log(f"Tentativa de voto inválido | CPF: {estado.cpf_eleitor}")
                return
            else:
                print(f"\nCandidato: {candidato_existe[1]}")
            
            #Inserindo o voto no MySQL
            #Query de Update para inserir o voto na tabela votos
            cpf_completo = estado.eleitor[0]

            query_update = """
            UPDATE eleitores 
            SET status_ele = 1 
            WHERE cpf_ele = %s
            """
            estado.cursor.execute(query_update, (cpf_completo,))

            # Salvando alterações no banco
            estado.connection.commit()
            print("Voto registrado com sucesso!")
            v.gerar_protocolo(voto)
            query_voto = """
            INSERT INTO votos (num_cand, nome_cand, protocolo)
            VALUES (%s, %s, %s)
            """
            estado.cursor.execute(query_voto, ( voto, candidato_existe[1], estado.protocolo))
            estado.connection.commit()
            #Registrando no Log de votações
            registrar_log(f"Voto registrado | Candidato: {voto} | Protocolo de Votacao: {estado.protocolo}\n")

            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()

            #Menu de Sistema de Votação
            menu_sistem_votacao_func()

        #Fazendo o except para caso haja erros durante o processo
        except Exception as erro: #Ao usar "AS ERRO" a causa do erro é salva em uma variável
            print(f"Erro durante votação")

            #Registrando erro no log
            registrar_log(f"Erro durante votação: {erro}")

        finally: #O finally é a terceira causa do TRY e serve para executar o ultimo comando quando acaba o bloco que deseja executar
            #serve para executar um bloco de código independentemente de dar erro ou não.
            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()



"""Menu Votação"""
def menu_votacao_func():
    while estado.menu_principal == 2:
        try:
            print("0 - Voltar \n1 - Começar a votação \n2 - Auditoria \n3 - Resultado")
            estado.menu_votacao= int(input("Escolha a opção desejada: "))
            match estado.menu_votacao:
                case 0:
                    import menu_principal as main
                    print("\n Voltando... ")
                    return(main.menu_principal_func())
                case 1:
                    #Eleitor[4] = Mesario
                    print("Começar a votação")
                    v.login_func()
                    if estado.eleitor[4] == True:
                        if estado.sistema_votacao_aberto == False:
                            db.conecta_mysql()
                            query_zere_votos = """
                            DELETE FROM votos
                            """
                            estado.cursor.execute(query_zere_votos)
                            estado.connection.commit()
                            estado.sistema_votacao_aberto = True
                            query_reset = """
                            UPDATE eleitores 
                            SET status_ele = 0
                            """
                            estado.cursor.execute(query_reset)
                            estado.connection.commit()
                            menu_sistem_votacao_func()
                            break
                        else:
                            print("Sistema de votação ja aberto!")
                            return
                    else:
                        print("Eleitor Comum")
                        print("Apenas eleitores mesarios podem iniciar o sistema de votação.")
                        return
                case 2:
                    print("Auditoria")
                    menu_auditoria_func()
                    break
                case 3:
                    print("Resultado")
                    menu_resultado_func()
                    break
                case _:
                    print("Opção Invalida, tente novamente.")
        except ValueError:
            print("Entrada Inválida. Digite um Numero")


"""Auditoria"""
def menu_auditoria_func():
    while estado.menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Exibir Logs \n2 - Deletar Logs")
            estado.menu_auditoria= int(input("Escolha a opção desejada: "))
            match estado.menu_auditoria:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Exibindo Logs")
                    try:
                        with open("logs.txt", "r", encoding="utf-8") as arquivo:
                            conteudo = arquivo.read()

                        if conteudo == "":
                            print("Nenhum log encontrado.")
                        else:
                            print("\n===== LOGS DO SISTEMA =====\n")
                            print(conteudo)
                    except FileNotFoundError:
                        print("Arquivo de logs não encontrado!")
                case 2:
                    print("Deletando Logs...")
                    with open("logs.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.write("")

                    print("Logs apagados com sucesso!")
                    import menu_principal as main
                    return main.menu_principal_func()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Sistema De Votação"""
def menu_sistem_votacao_func():
    
    while estado.menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Votar\n2 - Fechar Sistema de Votação")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            db.conecta_mysql()
            match menu_sistem_votacao:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    v.login_func()
                    if estado.eleitor[3] == False:
                        realizar_votacao_func() 
                        break
                    else:
                        print("Esse Eleitor ja votou!")
                        menu_sistem_votacao_func()
                case 2:
                        if estado.sistema_votacao_aberto == False:
                            print("Sistema de votação ja fechado!")
                            menu_votacao_func()
                        else:
                            #Variável global de controle, para não ter erros
                            v.login_func() 
                            if estado.eleitor[4] == False:
                                print("Eleitor Comum")
                                print("Apenas eleitores mesarios podem fechar o sistema de votação.")
                                return
                            else:
                                #Registrando log
                                estado.sistema_votacao_aberto = False
                                registrar_log("Sistema de votação encerrado")
                                print("Encerrando Sistema de Votação...")

                                menu_votacao_func()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
        finally:
            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()

""""Menu Resultado"""
def menu_resultado_func():

    while estado.menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna")
            estado.menu_resultado= int(input("Escolha a opção desejada: "))
            match estado.menu_resultado:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Boletim de Urna")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

