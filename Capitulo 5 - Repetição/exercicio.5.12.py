# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
deposito_mensal = float(input("Digite o valor depositado mensalmente: "))
meses = 24 
total = deposito_inicial
print(f"{'Mês':<5} {'Valor':<10} {'Total':<10}") # Cabeçalhos para a tabela
while meses > 0:
    total += deposito_mensal
    juros = total * (taxa_juros / 100)
    total += juros
    print(f"{24 - meses + 1:<5} {juros:<10.2f} {total:<10.2f}")
    meses -= 1
print(f"Total ganho com juros: {total - deposito_inicial:.2f}")
