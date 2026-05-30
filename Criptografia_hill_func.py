"""
Módulo de Criptografia.

Implementa a Cifra de Hill utilizando um alfabeto expandido
composto por letras maiúsculas e dígitos numéricos, permitindo
a criptografia de CPFs, senhas, protocolos e demais informações
utilizadas pelo sistema eleitoral.
"""

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MOD = len(alfabeto)  # 36
 
# Passando de caractere para número: usa o INDEX() que procura a posição do caractere
def letra_para_numero(letra):

    """
    Converte um caractere do alfabeto suportado para sua posição numérica.

    A função localiza a posição de uma letra ou dígito dentro do
    alfabeto utilizado pela Cifra de Hill.

    Args:
        letra (str): Caractere a ser convertido.

    Returns:
        int: Posição numérica correspondente ao caractere informado.
    """

    if letra not in alfabeto:
        raise ValueError(f"Caractere '{letra}' não está no alfabeto suportado.")
    return alfabeto.index(letra)
 
# Passando um número para caractere
def numero_para_letra(num):

    """
    Converte um valor numérico para o caractere correspondente.

    A função recebe um número e retorna o caractere equivalente
    dentro do alfabeto utilizado pela Cifra de Hill.

    Args:
        num (int): Valor numérico a ser convertido.

    Returns:
        str: Caractere correspondente ao valor informado.
    """

    return alfabeto[num % MOD]
 
def multiplicar_matriz(A, Vetor):

    """
    Realiza a multiplicação entre uma matriz chave e um vetor.

    A função executa a operação matricial necessária para o
    processo de criptografia da Cifra de Hill.

    Args:
        A (list): Matriz chave utilizada na criptografia.
        Vetor (list): Vetor contendo os valores numéricos do bloco.

    Returns:
        list: Vetor resultante da multiplicação modular.
    """

    # A representa a matriz chave
    # Vetor representa o bloco numérico
    x = A[0][0]*Vetor[0] + A[0][1]*Vetor[1]
    y = A[1][0]*Vetor[0] + A[1][1]*Vetor[1]
    return [x % MOD, y % MOD]
 
# Criptografando com cifra de Hill
def cifra_hill(texto, A):

    """
    Criptografa um texto utilizando o algoritmo da Cifra de Hill.

    A função converte os caracteres do texto em valores numéricos,
    realiza a multiplicação matricial utilizando a matriz chave e
    gera o texto criptografado correspondente.

    Args:
        texto (str): Texto a ser criptografado.
        A (list): Matriz chave utilizada na criptografia.

    Returns:
        str: Texto criptografado utilizando a Cifra de Hill.
    """

    # Remove espaços, hífens e pontos (comum em CPF) e converte para maiúsculo
    texto = texto.replace(" ", "").replace("-", "").replace(".", "").upper()
 
    # Verifica se todos os caracteres estão no alfabeto suportado
    for char in texto:
        if char not in alfabeto:
            raise ValueError(f"Caractere '{char}' não suportado pela cifra.")
 
    # Se o número de caracteres for ímpar, adiciona padding
    if len(texto) % 2 != 0:
        texto += "0"  # Usa "0" como padding (mais neutro que "X" para textos numéricos)
 
    resultado = ""
 
    for i in range(0, len(texto), 2):
        bloco = [letra_para_numero(texto[i]), letra_para_numero(texto[i+1])]
        cifrado = multiplicar_matriz(A, bloco)
        resultado += numero_para_letra(cifrado[0])
        resultado += numero_para_letra(cifrado[1])
 
    return resultado

