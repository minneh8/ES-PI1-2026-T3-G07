import Criptografia_hill_func as crypt # Importando todas funções do código de criptografia

#A função segue a mesma ideia, porém, dessa vez, os blocos serão multiplicados pela matriz inversa da matriz chave
def decifra_hill (texto, A_inv):
    texto = texto.replace(" ", "").upper()
    
    resultado = ""
    
    for i in range(0, len(texto), 2):
        bloco = [crypt.letra_para_numero(texto[i]), crypt.letra_para_numero(texto[i+1])]
        
        decifrado = crypt.multiplicar_matriz(A_inv, bloco) # Multiplica o bloco pela matriz inversa
        
        resultado += crypt.numero_para_letra(decifrado[0])
        resultado += crypt.numero_para_letra(decifrado[1])
    
    return resultado

