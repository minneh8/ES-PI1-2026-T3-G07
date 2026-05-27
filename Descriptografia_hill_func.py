#Importando funções do arquivo de criptografia
import Criptografia_hill_func as crypt

#Função principal de descriptografia
def decifra_hill(texto, matriz_inversa):

    #Padronizando texto
    texto = texto.replace(" ", "").upper()

    #Variável para armazenar resultado final
    resultado = ""

    #Percorrendo texto de 2 em 2
    for i in range(0, len(texto), 2):

        #Transformando caracteres em números
        bloco = [
            crypt.caractere_para_numero(texto[i]),
            crypt.caractere_para_numero(texto[i + 1])
        ]

        #Multiplicando bloco pela matriz inversa
        decifrado = crypt.multiplicar_matriz(matriz_inversa, bloco)

        #Convertendo novamente para caracteres
        resultado += crypt.numero_para_caractere(decifrado[0])
        resultado += crypt.numero_para_caractere(decifrado[1])

    #Remove X extra do final
    if resultado[-1] == "X":
        resultado = resultado[:-1]
    #Retornando texto descriptografado
    return resultado