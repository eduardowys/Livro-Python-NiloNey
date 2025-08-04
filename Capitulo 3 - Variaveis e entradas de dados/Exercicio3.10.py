# Exercício 3.10 – Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite o valor do salário: "))  # Entrada do valor do salário
percentual_aumento = float(input("Digite a porcentagem do aumento: "))  # Entrada da porcentagem do aumento
aumento = salario * (percentual_aumento / 100)  # Cálculo do aumento
novo_salario = salario + aumento  # Cálculo do novo salário
print(f"O valor do aumento é de R$ {aumento:.2f} e o novo salário é de R$ {novo_salario:.2f}")  # Exibe o valor do aumento
