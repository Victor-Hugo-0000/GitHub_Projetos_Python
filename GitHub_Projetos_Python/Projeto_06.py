# 6 - Verificando Palíndromos

palavra = input("Digite uma palavra: ").strip().lower()
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")