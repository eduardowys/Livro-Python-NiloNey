# Exercício 4.14 - Reescreva o programa abaixo com if-elif-else:
# if a < 10:
#     print("a é menor que 10")
# if a >= 10 and a < 20:
#     print("a é maior que 10 e menor que 20")
# if a >= 20:
#     print("a é maior que 20")
a = int(input("Digite um valor para a: "))
if a < 10:
    print("a é menor que 10")
elif a >= 10 and a < 20:
    print("a é maior que 10 e menor que 20")
elif a >= 20:
    print("a é maior que 20")
else:
    print("Valor inválido")