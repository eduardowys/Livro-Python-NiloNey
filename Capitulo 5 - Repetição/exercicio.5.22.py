# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, multiplicação, divisão e sair.
# Imprima a tabuada de operações escolhidas pelo usuário, repita até que o usuário escolha sair.
while True:
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação: ")

    if escolha == '5':
        print("Saindo do programa.")
        break

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida, tente novamente.")
        continue

    numero = int(input("Digite um número para ver a tabuada: "))

    for i in range(1, 11):
        if escolha == '1':
            resultado = numero + i
            operacao = "+"
        elif escolha == '2':
            resultado = numero - i
            operacao = "-"
        elif escolha == '3':
            resultado = numero * i
            operacao = "*"
        elif escolha == '4':
            if i == 0:
                resultado = "Indefinido (divisão por zero)"
            else:
                resultado = numero / i
                operacao = "/"

        print(f"{numero} {operacao} {i} = {resultado}")