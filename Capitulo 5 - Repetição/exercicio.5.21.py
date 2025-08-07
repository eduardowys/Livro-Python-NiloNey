# Rescreva o programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize a repetição aninhada.
while True:
    valor = float(input("Digite o valor a pagar (0 para sair): "))
    if valor == 0:
        break
    apagar = valor
    atual = 100
    cedulas = 0

    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            if cedulas > 0:
                print(f"{cedulas} cédula(s) de R$ {atual:.2f}")
            if round(apagar, 2) == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            cedulas = 0