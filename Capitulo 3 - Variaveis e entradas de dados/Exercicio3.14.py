# Exercício 3.14 – Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
km_percorridos = float(input("Digite a quantidade de km percorridos: "))  # Entrada da quantidade de km percorridos
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))  # Entrada da quantidade de dias alugados
preco_por_dia = 60.0  # Preço por dia de aluguel do carro
preco_por_km = 0.15  # Preço por km rodado
preco_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)  # Cálculo do preço total a pagar
print(f"O preço total a pagar pelo aluguel do carro é de R$ {preco_total:.2f}")  # Exibe o preço total a pagar pelo aluguel do carro    