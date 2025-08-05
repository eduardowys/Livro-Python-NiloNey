# Escreva um programa que pergunta o salário de um funcionário. O programa deve calcular e exibir o novo salário, aplicando um aumento de 15% para quem ganha até R$ 1.250,00 (inclusive), e um aumento de 10% para quem ganha acima desse valor
salario = float(input('Digite o salário do funcionário: R$ '))
if salario <= 1250.00:
    novo_salario = salario * 1.15
if salario > 1250.00:
    novo_salario = salario * 1.10   
print(f'O novo salário é: R$ {novo_salario:.2f}')