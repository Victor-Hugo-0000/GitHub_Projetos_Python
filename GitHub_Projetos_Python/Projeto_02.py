# 2 - Repetindo Textos

texto = input("Digite um texto: ")
num = int(input("Digite um número inteiro: "))

textrepete = (", ".join([texto] * num))

print("Texto repetido:",textrepete)