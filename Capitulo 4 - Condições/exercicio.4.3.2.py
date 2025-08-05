# Escreva um programa que leia 3 números e que imprima o maior e o menor.
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c
if a <= b and a <= c:
    menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')     