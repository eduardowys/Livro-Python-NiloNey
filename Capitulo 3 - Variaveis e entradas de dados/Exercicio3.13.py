# Exercício 3.13 – Escreva um programa que converta uma temperatura digitada em °C para °F. A fórmula para essa conversão é: F = (9 × C / 5) + 32
celsius = float(input("Digite a temperatura em °C: "))  # Entrada da temperatura em °C
fahrenheit = (9 * celsius / 5) + 32  # Cálculo da temperatura em °F
print(f"A temperatura em °F é: {fahrenheit:.2f}")  # Exibe a temperatura convertida em °F   