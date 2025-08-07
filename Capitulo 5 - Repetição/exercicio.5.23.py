# Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão
# do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número
# não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
numero = int(input("Digite um número: "))
if numero < 2:
    print(f"{numero} não é primo.")
else:
    primo = True
    if numero == 2:
        primo = True
    elif numero % 2 == 0:
        primo = False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                primo = False
                break
    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
# Fim do código