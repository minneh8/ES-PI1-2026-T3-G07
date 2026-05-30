"""
Módulo de Descriptografia.

Implementa a descriptografia utilizando a Cifra de Hill,
permitindo recuperar informações previamente criptografadas
como CPFs, senhas e protocolos armazenados pelo sistema.
"""

#Importando funções do arquivo de criptografia
import Criptografia_hill_func as crypt

#Função principal de descriptografia
def decifra_hill(texto, matriz_inversa):

    """
    Descriptografa um texto utilizando a Cifra de Hill.

    A função converte os caracteres criptografados em valores
    numéricos, realiza a multiplicação pela matriz inversa da
    chave utilizada na criptografia e retorna o texto original.

    Args:
        texto (str): Texto criptografado a ser descriptografado.
        matriz_inversa (list): Matriz inversa da chave utilizada
            na Cifra de Hill.

    Returns:
        str: Texto descriptografado.
    """
        
    #Padronizando texto
    texto = texto.replace(" ", "").upper()

    #Variável para armazenar resultado final
    resultado = ""

    #Percorrendo texto de 2 em 2
    for i in range(0, len(texto), 2):

        #Transformando caracteres em números
        bloco = [
            crypt.letra_para_numero(texto[i]),
            crypt.letra_para_numero(texto[i + 1])
        ]

        #Multiplicando bloco pela matriz inversa
        decifrado = crypt.multiplicar_matriz(matriz_inversa, bloco)

        #Convertendo novamente para caracteres
        resultado += crypt.numero_para_letra(decifrado[0])
        resultado += crypt.numero_para_letra(decifrado[1])

    #Remove X extra do final
    if resultado[-1] == "X":
        resultado = resultado[:-1]
    #Retornando texto descriptografado
    return resultado

