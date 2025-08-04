# Exercício 3.12 – Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Digite a distância a percorrer (em km): "))  # Entrada da distância em km
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))  # Entrada da velocidade média em km/h
tempo_viagem = distancia / velocidade_media  # Cálculo do tempo de viagem em horas
print(f"O tempo estimado para a viagem é de {tempo_viagem:.2f} horas")  # Exibe o tempo estimado para a viagem