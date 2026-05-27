# Cifra de Hill - Criptografia
# Deve-se seguir o seguinte fluxo: letras -> números -> blocos -> multiplicação -> mod 36 -> caracteres
 
# Alfabeto expandido: letras maiúsculas + dígitos (total 36 caracteres)
# Isso permite cifrar CPFs, senhas e outros textos que contenham números
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MOD = len(alfabeto)  # 36
 
# Passando de caractere para número: usa o INDEX() que procura a posição do caractere
def letra_para_numero(letra):
    if letra not in alfabeto:
        raise ValueError(f"Caractere '{letra}' não está no alfabeto suportado.")
    return alfabeto.index(letra)
 
# Passando um número para caractere
def numero_para_letra(num):
    return alfabeto[num % MOD]
 
def multiplicar_matriz(A, Vetor):
    # A representa a matriz chave
    # Vetor representa o bloco numérico
    x = A[0][0]*Vetor[0] + A[0][1]*Vetor[1]
    y = A[1][0]*Vetor[0] + A[1][1]*Vetor[1]
    return [x % MOD, y % MOD]
 
# Criptografando com cifra de Hill
def cifra_hill(texto, A):
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