#Importando biblioteca numpy para trabalhar com matrizes
import numpy as np

#Criando tabela de referência com letras e números
#Agora também iremos aceitar números de 0 até 9
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#Função responsável por converter uma letra/número em posição numérica
def caractere_para_numero(caractere):

    #O método .index() procura a posição do caractere dentro da string
    return alfabeto.index(caractere)

#Função responsável por converter posição numérica em letra/número
def numero_para_caractere(numero):

    #O MOD 36 é utilizado porque agora existem:
    #26 letras + 10 números = 36 caracteres
    return alfabeto[numero % 36]

#Função responsável por multiplicar a matriz chave pelo bloco numérico
def multiplicar_matriz(matriz, vetor):

    #Transformando lista comum em arrays numpy
    matriz_np = np.array(matriz)
    vetor_np = np.array(vetor)

    #Realizando multiplicação de matriz
    resultado = np.dot(matriz_np, vetor_np)

    #Aplicando MOD 36 em todos valores
    resultado = resultado % 36

    #Convertendo novamente para lista comum
    return resultado.tolist()

#Função principal de criptografia
def cifra_hill(texto, matriz_chave):

    #Padronizando texto:
    #Removendo espaços
    #Transformando em maiúsculo
    texto = texto.replace(" ", "").upper()

    #Verificando se todos caracteres existem na tabela
    for caractere in texto:
        if caractere not in alfabeto:
            raise ValueError(f"Caractere inválido: {caractere}")

    #A cifra trabalha em blocos de 2 caracteres
    #Se quantidade for ímpar, adiciona X no final
    if len(texto) % 2 != 0:
        texto += "X"

    #Variável que armazenará resultado final
    resultado = ""

    #Loop percorrendo o texto de 2 em 2
    for i in range(0, len(texto), 2):
        #Separando bloco atual
        bloco = [
            caractere_para_numero(texto[i]),
            caractere_para_numero(texto[i + 1])
        ]

        #Multiplicando bloco pela matriz chave
        cifrado = multiplicar_matriz(matriz_chave, bloco)

        #Convertendo números novamente para caracteres
        resultado += numero_para_caractere(cifrado[0])
        resultado += numero_para_caractere(cifrado[1])

    #Retornando texto criptografado
    return resultado