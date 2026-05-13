# Validação do CPF do usuário
import CondicoesGlobais as cg
def validacao_cpf_func(cpf):   
    
    """ Validação do CPF, onde o usuário digita o número e o programa verifica se é um CPF """
    """ N = Números do CPF """
    # D = Digito Verificador do CPF 
    n1 = int(cg.cpf[0])
    n2 = int(cg.cpf[1])
    n3 = int(cg.cpf[2])
    n4 = int(cg.cpf[3])
    n5 = int(cg.cpf[4])
    n6 = int(cg.cpf[5])
    n7 = int(cg.cpf[6])
    n8 = int(cg.cpf[7])
    n9 = int(cg.cpf[8])
    d1 = int(cg.cpf[9])
    d2 = int(cg.cpf[10])

    # Verificação de dígito
    # Dígito 1
    verifd1 = ((n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2) % 11)
    if verifd1 < 2:
        verifd1 = 0
        if verifd1 == d1:
            verifd2 = ((n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + d1 * 2) % 11)
            if verifd2 < 2:
                verifd2 = 0
            elif verifd2 >= 2:
                verifd2 = 11 - verifd2
                if verifd2 == d2:
                    print("CPF Válido!")
                    cg.cpfvalido = True
                else:
                    print("CPF Inválido! ")
                    cg.cpfvalido = False
        else:
            print("CPF Inválido! ")
            cg.cpfvalido = False

    # Dígito 2
    if verifd1 >= 2:
        verifd1 = 11 - verifd1
        if verifd1 == d1:
            verifd2 = ((n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + d1 * 2) % 11)
            if verifd2 < 2:
                verifd2 = 0
            elif verifd2 >= 2:
                verifd2 = 11 - verifd2
                if verifd2 == d2:
                    print("CPF Válido!")
                    cg.cpfvalido = True      
                else:
                    print("CPF Inválido!")
                    cg.cpfvalido = False
        else:
            print("CPF Inválido!")
            cg.cpfvalido = False

# Validação do Título de Eleitor do Usuário
def validacao_tituloeleitor_func (teleitor):

    while len(cg.teleitor) != 12:
        print("Titulo Eleitor inválido. O Titulo Eleitor deve conter exatamente 12 dígitos numéricos.")
        cg.teleitor = input("Digite o seu Titulo Eleitor: ")

    # N = Número do título
    # E = Dígito de estado
    # D = Dígito Verificador
    n1 = int(cg.teleitor[0])
    n2 = int(cg.teleitor[1])
    n3 = int(cg.teleitor[2])
    n4 = int(cg.teleitor[3])
    n5 = int(cg.teleitor[4])
    n6 = int(cg.teleitor[5])
    n7 = int(cg.teleitor[6])
    n8 = int(cg.teleitor[7])

    e9 = int(cg.teleitor[8])
    e10 = int(cg.teleitor[9])
    
    d11 = int(cg.teleitor[10])
    d12 = int(cg.teleitor[11])

    estado_cod = str(str(e9) + str(e10)) #Juntando os dígitos e9 e e10 em uma só string

    #Dicionário para guardar sigla do estado para cada digito de estado

    estados = {
        "01": "SP", "02": "MG", "03": "RJ", "04": "RS",
        "05": "BA", "06": "PR", "07": "CE", "08": "PE",
        "09": "SC", "10": "GO", "11": "MA", "12": "PB",
        "13": "PA", "14": "ES", "15": "PI", "16": "RN",
        "17": "AL", "18": "MT", "19": "MS", "20": "DF",
        "21": "SE", "22": "AM", "23": "RO", "24": "AC",
        "25": "AP", "26": "RR", "27": "TO", "28": "ZZ",
        }

     # Verificando se o estado existe na lista
    if (estado_cod not in estados): # SE o código dos estados NÃO ESTÁ no dict
        print("Estado inválido")

    cg.estado = estados[estado_cod] # Definindo o estado para o conjunto de números recebidos
    
    verifd1 = ((n1 * 2 + n2 * 3 + n3 * 4 + n4 * 5 + n5 * 6 + n6 * 7 + n7 * 8 + n8 * 9) % 11)
    verifd2 = ((e9 * 7 + e10 * 8 + d11 * 9) % 11)

    if verifd1 == d11 and verifd2 == d12:
        print(f"Título Eleitor Válido! \t Seu Estado: {cg.estado}")
        cg.teleitorvalido = True
    else: 
        print("Titulo de Eleitor inválido!")
        cg.teleitorvalido = False
    # Verificação de dígito
    # Aqui será feito o código de verificação

def gerador_senha_func():
    import random

    partes = cg.nome.split()  # Separa pelo espaço
    primeiro_nome = partes[0]
    segundo_nome = partes[1]

    # Três primeiras letras
    letra1 = primeiro_nome[0].upper()   # 1ª letra do primeiro nome
    letra2 = primeiro_nome[1].upper()   # 2ª letra do primeiro nome
    letra3 = segundo_nome[0].upper()    # 1ª letra do segundo nome

    # 4 números aleatórios
    numeros = ''.join([str(random.randint(0, 9)) for _ in range(4)])

    cg.senha = letra1 + letra2 + letra3 + numeros



def gerar_protocolo(voto):
    import random
    import string
    # "V" + 2 letras aleatórias + Ano (26) + número candidato (2 dígitos) + 5 dígitos aleatórios
    prefixo = "V"
    letras_aleatorias = ''.join(random.choices(string.ascii_uppercase, k=2))
    ano = "26"
    candidato_formatado = str(voto).zfill(2)  # Garante 2 dígitos ex: 4 -> "04"
    digitos_aleatorios = ''.join(random.choices(string.digits, k=5))

    cg.protocolo = f"{prefixo}{letras_aleatorias}{ano}{candidato_formatado}{digitos_aleatorios}"
    print(f"Seu Protocolo de Votação: {cg.protocolo}")


    



