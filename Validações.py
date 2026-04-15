import CondicoesGlobais as estado


def validacao_cpf_func():   
        cpf = input("Digite o seu CPF: ")
        while len(cpf) != 11:
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
            cpf = input("Digite o seu CPF: ")
        """Validação do CPF, onde o usuário digita o número e o programa verifica se é um CPF, Sendo N = Números do CPF e D = Digito Verificador do CPF """
        n1 = int(cpf[0])
        n2 = int(cpf[1])
        n3 = int(cpf[2])
        n4 = int(cpf[3])
        n5 = int(cpf[4])
        n6 = int(cpf[5])
        n7 = int(cpf[6])
        n8 = int(cpf[7])
        n9 = int(cpf[8])
        d1 = int(cpf[9])
        d2 = int(cpf[10])

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
                    else:
                        print("CPF Inválido! O segundo dígito verificador está incorreto.")
            else:
                print("CPF Inválido! O primeiro dígito verificador está incorreto.")
 
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
                    
                    else:
                        print("CPF Inválido! O segundo dígito verificador está incorreto.")
            else:
                print("CPF Inválido! O primeiro dígito verificador está incorreto.")


def validacao_tituloeleitor_func():
    teleitor = input("Digite o seu Titulo Eleitor: ")
    while len(teleitor) != 12:
        print("Titulo Eleitor inválido. O Titulo Eleitor deve conter exatamente 12 dígitos numéricos.")
        teleitor = input("Digite o seu Titulo Eleitor: ")

    n1 = int(teleitor[0])
    n2 = int(teleitor[1])
    n3 = int(teleitor[2])
    n4 = int(teleitor[3])
    n5 = int(teleitor[4])
    n6 = int(teleitor[5])
    n7 = int(teleitor[6])
    n8 = int(teleitor[7])
    e9 = str(teleitor[8])
    e10 = str(teleitor[9])
    d11 = int(teleitor[10])
    d12 = int(teleitor[11])

    estado = str(e9 + e10)
    dict = {
        "01": "SP",
        "02": "MG",
        "03": "RJ",
        "04": "RS",
        "05": "BA",
        "06": "PR",
        "07": "CE",
        "08": "PE",
        "09": "SC",
        "10": "GO",
        "11": "MA",
        "12": "PB",
        "13": "PA",
        "14": "ES",
        "15": "PI",
        "16": "RN",
        "17": "AL",
        "18": "MT",
        "19": "MS",
        "20": "DF",
        "21": "SE",
        "22": "AM",
        "23": "RO",
        "24": "AC",
        "25": "AP",
        "26": "RR",
        "27": "TO",
        "28": "ZZ",
        }
    estado = dict[estado]
    

validacao_tituloeleitor_func()