import CondicoesGlobais as estado
import Validações as v
def tela_login_func():
    print("""
:'######::'####::'######::'########:'########:'##::::'##::::'###:::::::'########::'########::::'##::::'##::'#######::'########::::'###:::::'######:::::'###:::::'#######::
'##... ##:. ##::'##... ##:... ##..:: ##.....:: ###::'###:::'## ##:::::: ##.... ##: ##.....::::: ##:::: ##:'##.... ##:... ##..::::'## ##:::'##... ##:::'## ##:::'##.... ##:
 ##:::..::: ##:: ##:::..::::: ##:::: ##::::::: ####'####::'##:. ##::::: ##:::: ##: ##:::::::::: ##:::: ##: ##:::: ##:::: ##:::::'##:. ##:: ##:::..:::'##:. ##:: ##:::: ##:
. ######::: ##::. ######::::: ##:::: ######::: ## ### ##:'##:::. ##:::: ##:::: ##: ######:::::: ##:::: ##: ##:::: ##:::: ##::::'##:::. ##: ##:::::::'##:::. ##: ##:::: ##:
:..... ##:: ##:::..... ##:::: ##:::: ##...:::: ##. #: ##: #########:::: ##:::: ##: ##...:::::::. ##:: ##:: ##:::: ##:::: ##:::: #########: ##::::::: #########: ##:::: ##:
'##::: ##:: ##::'##::: ##:::: ##:::: ##::::::: ##:.:: ##: ##.... ##:::: ##:::: ##: ##:::::::::::. ## ##::: ##:::: ##:::: ##:::: ##.... ##: ##::: ##: ##.... ##: ##:::: ##:
. ######::'####:. ######::::: ##:::: ########: ##:::: ##: ##:::: ##:::: ########:: ########::::::. ###::::. #######::::: ##:::: ##:::: ##:. ######:: ##:::: ##:. #######::
:......:::....:::......::::::..:::::........::..:::::..::..:::::..:::::........:::........::::::::...::::::.......::::::..:::::..:::::..:::......:::..:::::..:::.......:::
                                                                                                                                                                          
                                                                                                                                                                          

""")
    
    print("Seja bem vindo ao nosso sistema de votação!\nPara prosseguir, por favor, faça login ou o seu cadastro.\n\n1- Login\n2- Cadastro\n3- Sair\n")
    while estado.tela_login == -1:
        try:
            estado.tela_login = int(input("Escolha a opção desejada: "))
            match estado.tela_login:
                case 1:
                    print("Login")
                    login_func()
                    break
                case 2:
                    print("Cadastro")
                    cadastro_func()
                    break
                case 3:
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
def login_func():
    print("Login")

def cadastro_func():
    print("Para realizar o cadastro, por favor, digite o seu Nome, Sobrenome, CPF, Titulo Eleitoral.\nSua Senha será gerada automaticamente.\n")
    estado.nome = input("Digite o seu Nome: ")
    estado.sobrenome = input("Digite o seu Sobrenome: ")
    estado.cpf = input("Digite o seu CPF: ")
    match len(estado.cpf) == 11:
        case True:
            v.validacao_cpf_func(estado.cpf)
        case False:
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
    estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
    match len(estado.teleitor) == 12:
        case True:
            v.validacao_tituloeleitor_func(estado.teleitor)
        case False:
            print("Titulo Eleitor inválido. O Titulo Eleitor deve conter exatamente 12 dígitos numéricos.")
tela_login_func()