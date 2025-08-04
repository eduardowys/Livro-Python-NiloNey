# Escreva um programa que lê a quantidade de dias horas minutos e segundos do usuário calcule o total em segundos
dias = int(input("Digite a quantidade de dias: "))  # Entrada da quantidade de dias
horas = int(input("Digite a quantidade de horas: "))  # Entrada da quantidade de horas
minutos = int(input("Digite a quantidade de minutos: "))  # Entrada da quantidade de minutos
segundos = int(input("Digite a quantidade de segundos: "))  # Entrada da quantidade de segundos
total_em_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos  # Cálculo do total em segundos
print(f"O total em segundos é: {total_em_segundos}")  # Exibe o total em segundos