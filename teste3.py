# Alfabeto original e cifrado definidos manualmente


# Função para criptografar uma frase
def criptografar_rustico(frase):
    frase_criptografada = ""
    for caractere in frase:
        if caractere in alfabeto_original:  # Verifica se o caractere é uma letra minúscula
            # Busca manualmente a posição do caractere no alfabeto original
            for i in range(len(alfabeto_original)):
                if alfabeto_original[i] == caractere:
                    # Substitui pelo caractere correspondente no alfabeto cifrado
                    frase_criptografada += alfabeto_cifrado[i]
                    break
        else:
            # Mantém caracteres que não são letras (espaços, pontuação, etc.)
            frase_criptografada += caractere
    return frase_criptografada
alfabeto_original = "abcdefghijklmnopqrstuvwxyz"
alfabeto_cifrado = "qwertyuiopasdfghjklzxcvbnm"
# Leitura da frase pelo usuário
frase = input("Digite a frase a ser criptografada: ").lower()  # Convertendo tudo para minúsculas para facilitar

# Criptografando a frase
frase_criptografada = criptografar_rustico(frase)

# Exibindo a frase criptografada
print("Frase criptografada:", frase_criptografada)
