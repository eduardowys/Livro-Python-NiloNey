# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
divida = float(input("Digite o valor inicial da dívida: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))
pagamento = float(input("Digite o valor pago mensalmente: "))

meses = 0
total_pago = 0
total_juros = 0

while divida > 0:
    juros = divida * (juros_mensal / 100)
    total_juros += juros
    divida += juros
    divida -= pagamento
    total_pago += pagamento
    meses += 1

print(f"Número de meses: {meses}")
print(f"Total pago: {total_pago:.2f}")
print(f"Total de juros: {total_juros:.2f}")