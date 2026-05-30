"""
Módulo de Votação.

Responsável pelo gerenciamento do processo eleitoral,
incluindo abertura e encerramento da votação, registro
de votos, auditoria, geração de logs, exibição de
resultados e validação da integridade dos dados.

O módulo também realiza consultas ao banco de dados e
utiliza criptografia para garantir a segurança das
informações armazenadas.
"""

import CondicoesGlobais as estado
from datetime import datetime
import DATABASE as db
import Validações as v
import Criptografia_hill_func as crypt
import Descriptografia_hill_func as decrypt

def registrar_log(mensagem):

    """
    Registra eventos no arquivo de log do sistema.

    A função grava uma mensagem acompanhada da data e
    hora da ocorrência, permitindo auditoria das ações
    realizadas durante o processo eleitoral.

    Args:
        mensagem (str): Mensagem que será registrada no log.

    Returns:
        None
    """

    with open("logs.txt", "a", encoding="utf-8") as arquivo: #Abrir arquivo logs.txt na UTF-8
        datahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Usando o import para salvar a data certa do computador convertendo em strings (STRF)
        arquivo.write(f"[{datahora}] {mensagem}\n") #Escrevendo no arquivo



def realizar_votacao_func():
        
        """
        Realiza o processo de votação de um eleitor.

        A função valida o candidato informado, permite a
        confirmação de voto nulo, atualiza o status do
        eleitor, gera um protocolo de votação criptografado
        e registra o voto no banco de dados.

        Args:
            None

        Returns:
            None
        """

        db.conecta_mysql()
        #Verificar se o sistema está aberto
        if estado.sistema_votacao_aberto == False:
            print("\nSistema de votação fechado! Você não pode votar agora.")
            return
        try:            
            print("\n===== VOTAÇÃO =====")
            estado.confirmar_voto = "N"
            while estado.confirmar_voto != "S":
                voto = input("Digite o número do candidato: ")        

                #Verificando se o candidato existe
                #Query para selecionar todos os candidatos do MySQL via número
                query_validacao = """
                SELECT candidatos.num,
                    candidatos.nome,
                    partidos.nome_partido
                FROM candidatos

                JOIN partidos
                ON candidatos.id_part = partidos.id_part

                WHERE candidatos.num = %s
                """
                
                estado.cursor.execute(query_validacao, (voto,))
                candidato_existe = estado.cursor.fetchone()

                #Caso o candidato não exista
                if candidato_existe == None:
                    print("\nCandidato não encontrado!")
                    # Voto nulo 
                    voto_nulo = input("Deseja confirmar VOTO NULO? (S/N)").upper()
                    if voto_nulo == "S":
                        estado.confirmar_voto = "S"
                        voto = "NULO"
                        candidato_nome = "NULO"
                    else:
                        print("Retornando para votação...")
                        continue
                #Caso o candidato exista

                else:
                    print("\n===== CONFIRMAÇÃO DE VOTO =====")
                    print(f"Nome: {candidato_existe[1]}")
                    print(f"Partido: {candidato_existe[2]}")
                    print(f"Número: {candidato_existe[0]}")
                    estado.confirmar_voto = input("\nConfirmar voto? (S/N): ").upper()

                    if estado.confirmar_voto == "N":
                        print("Voto cancelado!")
                        continue

                    candidato_nome = candidato_existe[1]

            #Inserindo o voto no MySQL
            #Query de Update para inserir o voto na tabela votos
            matrizcripto = [
                    [1, 1],
                    [0, 1]
                ]
            cpfcripto = crypt.cifra_hill(estado.cpf_eleitor, matrizcripto)

            query_update = """
            UPDATE eleitores 
            SET status_ele = 1 
            WHERE LEFT(cpf_ele, 4) = %s
            """
            estado.cursor.execute(query_update, (cpfcripto,))

            # Salvando alterações no banco
            estado.connection.commit()
            print("Voto registrado com sucesso!")
            v.gerar_protocolo(voto)
            matriz = [
                [1, 1],
                [0, 1]
            ]
            protocolocripto = crypt.cifra_hill(estado.protocolo, matriz)
            datahora_voto = datetime.now()
            query_voto = """
            INSERT INTO votos (num_cand, datahora_voto, protocolo)
            VALUES (%s, %s, %s)
            """
            estado.cursor.execute(query_voto, (voto, datahora_voto, protocolocripto))
            estado.connection.commit()
            #Registrando no Log de votações
            registrar_log(f"SUCESSO: Voto realizado com sucesso")

            #Menu de Sistema de Votação
            menu_sistem_votacao_func()

        #Fazendo o except para caso haja erros durante o processo
        except Exception as erro: #Ao usar "AS ERRO" a causa do erro é salva em uma variável
            print(f"Erro durante votação")

        finally: #O finally é a terceira causa do TRY e serve para executar o ultimo comando quando acaba o bloco que deseja executar
            #serve para executar um bloco de código independentemente de dar erro ou não.
            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()


def menu_votacao_func():

    """
    Exibe o menu principal de votação.

    Permite iniciar o sistema eleitoral, acessar a área
    de auditoria e consultar os resultados da eleição.

    Args:
        None

    Returns:
        None
    """
    
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
                    if estado.eleitor != None and estado.eleitor[4] == True:
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
                            registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
                            menu_sistem_votacao_func()
                        else:
                            print("Sistema de votação ja aberto!")
                            continue
                    else:
                        print("Login Incorreto")
                        print("Apenas eleitores mesarios podem iniciar o sistema de votação.")
                        registrar_log("ALERTA: Tentativa de acesso negado")
                        continue
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



def menu_auditoria_func():

    """
    Exibe o menu de auditoria do sistema.

    Permite consultar os logs de execução e visualizar
    os protocolos de votação armazenados no banco de
    dados após sua descriptografia.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Exibir Logs \n2 - Exibir Protocolos de Votação")
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
                        print("Arquivo de logs não encontrado")
                case 2:
                    #Exibir protocolos de votação
                    print("Exibindo Protocolos de Votação")
                    db.conecta_mysql()

                    cursor = estado.connection.cursor(dictionary=True)

                    query_protocolos = """
                    SELECT protocolo
                    FROM votos
                    ORDER BY protocolo ASC
                    """

                    cursor.execute(query_protocolos)

                    protocolos = cursor.fetchall()

                    # Matriz inversa da cifra de Hill
                    A_inv = [
                        [1, -1],
                        [0, 1]
                    ]

                    if not protocolos:
                        print("Nenhum protocolo encontrado.")

                    else:
                        for protocolo in protocolos:

                            protocolo_criptografado = protocolo["protocolo"]

                            protocolo_correto = decrypt.decifra_hill(protocolo_criptografado,A_inv)

                            print(protocolo_correto)

                    cursor.close()
                    estado.connection.close()
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_sistem_votacao_func():

    """
    Exibe o menu do sistema de votação.

    Permite que eleitores realizem seus votos e que
    mesários efetuem o encerramento oficial do processo
    eleitoral.

    Args:
        None

    Returns:
        None
    """

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
                    if estado.eleitor != None and estado.eleitor[3] == False:
                        realizar_votacao_func() 
                        break

                    elif estado.eleitor is None:
                        # Login falhou
                        print("Login Incorreto!")
                        registrar_log("ALERTA: Tentativa de acesso negado")
                        continue  
                    else:
                        print("Esse Eleitor ja votou!")
                        registrar_log("ALERTA: Tentativa de voto duplo")
                        continue  
                case 2:
                        if estado.sistema_votacao_aberto == False:
                            print("Sistema de votação ja fechado!")
                            menu_votacao_func()
                        else:
                            v.login_func() 
                            if estado.eleitor is None:  
                                print("Login Incorreto")
                                print("Apenas eleitores mesarios podem fechar o sistema de votação.")
                                registrar_log("ALERTA: Tentativa de acesso negado")
                                continue  # Volta ao loop

                            elif estado.eleitor[4] == False:  
                                print("Eleitor Comum")
                                print("Apenas eleitores mesarios podem fechar o sistema de votação.")
                                registrar_log("ALERTA: Tentativa de acesso negado")
                                continue

                            else:
                                estado.sistema_votacao_aberto = False
                                registrar_log("ENCERRAMENTO: Votação finalizada com sucesso")
                                print("Encerrando Sistema de Votação...")
                                continue 
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
        finally:
            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()

def menu_resultado_func():

    """
    Exibe o menu de resultados da eleição.

    Permite consultar o boletim de urna, estatísticas
    de comparecimento, votos por partido e validações
    de integridade dos dados registrados.

    Args:
        None

    Returns:
        None
    """

    while estado.menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna\n2 - Estatisticas\n3 - Votos por partido\n4 - Validação de Integridade")
            estado.menu_resultado= int(input("Escolha a opção desejada: "))
            match estado.menu_resultado:

                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                
                case 1:
                    # Boletim de urna:
                    # Consulta os votos de cada candidato,
                    # contabiliza votos nulos e identifica
                    # o candidato vencedor.

                    db.conecta_mysql()
                    estado.cursor = estado.connection.cursor(dictionary=True)
                    query_boletim = """
                    SELECT 
                    candidatos.nome,
                    candidatos.num,
                    partidos.nome_partido,
                    COUNT(votos.num_cand) AS total_votos

                    FROM candidatos

                    LEFT JOIN votos
                        ON candidatos.num = votos.num_cand

                    LEFT JOIN partidos
                        ON candidatos.id_part = partidos.id_part

                    GROUP BY 
                        candidatos.num,
                        candidatos.nome,
                        partidos.nome_partido

                    ORDER BY candidatos.nome ASC
                    """
                    estado.cursor.execute(query_boletim)
                    resultados = estado.cursor.fetchall()

                    query_nulos = """
                    SELECT COUNT(*) AS votos_nulos
                    FROM votos
                    WHERE num_cand = "NULO"
                    """

                    estado.cursor.execute(query_nulos)
                    votos_nulos = estado.cursor.fetchone()

                    print("\n===== BOLETIM DE URNA =====\n")
                    maior = -1
                    vencedor = None
                    for candidato in resultados:

                        print(
                            f"Nome: {candidato['nome']} | "
                            f"Número: {candidato['num']} | "
                            f"Partido: {candidato['nome_partido']} | "
                            f"Votos: {candidato['total_votos']}"
                            )

                        if candidato['total_votos'] > maior:
                            maior = candidato['total_votos']
                            vencedor = candidato

                    print(f"Quantidade de votos nulos: {votos_nulos['votos_nulos']}")

                    print("\n===== VENCEDOR =====\n")

                    print(
                        f"Nome: {vencedor['nome']} | "
                        f"Número: {vencedor['num']} | "
                        f"Partido: {vencedor['nome_partido']} | "
                        f"Votos: {vencedor['total_votos']}"
                    )

                    estado.cursor.close()
                    estado.connection.close()
                    
                case 2:
                    # Estatísticas:
                    # Exibe quantidade total de eleitores,
                    # eleitores que votaram e percentual
                    # de comparecimento.

                    db.conecta_mysql()
                    cursor = estado.connection.cursor()
                    query_total = """
                    SELECT COUNT(*) FROM eleitores
                    """
                    cursor.execute(query_total)
                    total_eleitores = cursor.fetchone()[0]

                    query_votaram = """
                    SELECT COUNT(*) FROM eleitores
                    WHERE status_ele = 1
                    """
                    cursor.execute(query_votaram)
                    total_votaram = cursor.fetchone()[0]
                    percentual = 0

                    if total_eleitores > 0:
                        percentual = (
                            total_votaram / total_eleitores
                        ) * 100

                    print("\n===== ESTATÍSTICAS =====\n")

                    print(f"Eleitores cadastrados: {total_eleitores}")
                    print(f"Eleitores que votaram: {total_votaram}")
                    print(f"Comparecimento: {percentual:.2f}%")

                    cursor.close()
                    estado.connection.close()
                
                case 3: 
                    # Votos por partido:
                    # Agrupa os votos recebidos por partido
                    # e ordena do mais votado para o menos votado.
                    
                   db.conecta_mysql() 
                   
                   cursor = estado.connection.cursor(dictionary=True) 
                   
                   query = """ SELECT partidos.nome_partido, 
                   COUNT(votos.num_cand) 
                   AS total_votos
                   
                   FROM votos 

                   JOIN candidatos 
                   ON votos.num_cand = candidatos.num 
                   
                   JOIN partidos 
                   ON candidatos.id_part = partidos.id_part 
                   
                   GROUP BY partidos.nome_partido 
                   
                   ORDER BY total_votos DESC """ 
                   
                   cursor.execute(query) 
                   
                   resultados = cursor.fetchall() 
                   
                   print("\n===== VOTOS POR PARTIDO =====\n") 
                   
                   for partido in resultados: 
                    
                     print( f"Partido: {partido['nome_partido']} "
                            f"| Votos: {partido['total_votos']}" ) 
                     
                   cursor.close() 
                   estado.connection.close()  

                case 4:
                    # Validação de integridade:
                    # Compara a quantidade de votos registrados
                    # com a quantidade de eleitores marcados
                    # como votantes.

                    db.conecta_mysql() 

                    cursor = estado.connection.cursor() 

                    query_votos = """ SELECT COUNT(*) 
                    FROM votos 
                    """ 

                    cursor.execute(query_votos) 
                    total_votos = cursor.fetchone()[0] 

                    query_eleitores = """ 
                    SELECT COUNT(*) 
                    FROM eleitores 
                    WHERE status_ele = 1 
                    """ 

                    cursor.execute(query_eleitores) 
                    total_eleitores = cursor.fetchone()[0] 

                    print("\n===== VALIDAÇÃO DE INTEGRIDADE =====\n") 
                    print(f"Votos registrados: {total_votos}") 

                    print( 
                        f'Eleitores com status "Já votou": '
                        f'{total_eleitores}'
                          ) 
                    if total_votos == total_eleitores: 
                        print("\nIntegridade validada com sucesso!") 
                    
                    else: 
                        print("\nALERTA DE INCONSISTÊNCIA!") 
                    
                    cursor.close() 
                    estado.connection.close() 

                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")