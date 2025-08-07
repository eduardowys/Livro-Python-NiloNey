# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.
n = int(input("Digite um número: "))
contador = 0
numero = 2
while contador < n:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero, end=' ')
        contador += 1
    numero += 1 
