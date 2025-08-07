# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = 0
while num2 > 0:
    resultado += num1
    num2 -= 1
print(f"O resultado da multiplicação é: {resultado}")