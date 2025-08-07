# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
inicio = int(input("Digite o início da tabuada de 2: "))
fim = int(input("Digite o fim da tabuada de 2: "))  
x = inicio
while x <= fim:
    print(f"2 x {x} = {2 * x}")
    x += 1