#Escreva um programa que leia um valor em metros e exiba o convertido em milimetros
metros = float(input("Digite o valor em metros: "))  # Entrada do valor em metros, convertido para float
milimetros = metros * 1000  # Converte metros para milímetros
print(f"{metros} metros equivalem a {milimetros:.0f} milímetros")  # Exibe o valor convertido