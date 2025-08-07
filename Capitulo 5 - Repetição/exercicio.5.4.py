# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
fim = int(input("Digite um número: "))
# Caso 1.
x = 1  # Inicia em 1 para garantir que comece com um número ímpar
while x <= fim:
    if x % 2 != 0:  # Verifica se o número é ímpar, para par deve ser x % 2 == 0
        print(x)
    x += 1  # Incrementa de 1 para verificar o próximo número
""" Caso 2.
x = 1  # 1 é o primeiro número ímpar, 0 é par.
while x <= fim: 
    print(x)
    x += 2  # Incrementa de 2 para pular os números pares
"""