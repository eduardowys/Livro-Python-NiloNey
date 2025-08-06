# Exercício 4.12 - Calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação (Residencial (R), Comercial (C) ou Industrial(I)). A tabela a seguir mostra o preço do kWh para cada tipo de instalação: 
# Residencial: até 500kwh R$ 0,40 e acima é R$ 0,65; Comercial: até 1000kwh é R$ 0,55 e acima é R$ 0,60; Industrial: até 5000kwh é R$ 0,55 e acima é R$ 0,60. Calcule o valor a pagar e exiba uma mensagem informando o tipo de instalação, a quantidade de kWh consumida e o valor a pagar.
consumo = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()
if tipo_instalacao == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo_instalacao == 'C':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo_instalacao == 'I':
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
else:
    print("Tipo de instalação inválido. Por favor, escolha R, C ou I.")

print("\nResumo da fatura:")
print(f"Tipo de instalação: {tipo_instalacao}")
print(f"Quantidade de kWh consumida: {consumo} kWh")
print(f"Valor a pagar: R$ {preco:.2f}")