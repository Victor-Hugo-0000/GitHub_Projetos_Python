# 3 - Operações Matemáticas Simples

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)