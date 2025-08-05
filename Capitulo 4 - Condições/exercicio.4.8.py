# Programa: Cálculo da mensalidade de um plano de celular da operadora Tchau

plano = input("Qual é o seu plano de celular? (falopouco/falomuito): ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco_base = 50
elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco_base = 99
else:
    print("Não conheço este plano.")
    exit()

minutos_consumidos = int(input("Quantos minutos você usou no mês? "))

if minutos_consumidos > minutos_no_plano:
    minutos_extras = minutos_consumidos - minutos_no_plano
    valor_total = preco_base + (minutos_extras * extra)
else:
    valor_total = preco_base

print(f"Valor a pagar: R$ {valor_total:.2f}")
