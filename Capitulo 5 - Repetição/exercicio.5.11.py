# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
meses = 24 
total = deposito_inicial
print(f"{'Mês':<5} {'Valor':<10} {'Total':<10}") # Cabeçalhos para a tabela
while meses > 0:
    juros = total * (taxa_juros / 100)
    total += juros
    print(f"{24 - meses + 1:<5} {juros:<10.2f} {total:<10.2f}")
    meses -= 1
print(f"Total ganho com juros: {total - deposito_inicial:.2f}")
