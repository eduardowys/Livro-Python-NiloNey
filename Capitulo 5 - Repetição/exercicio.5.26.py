# Escreva um programa que calcule o resto da divisão inteira entre dois números. 
# Utilize apenas as operações de soma e subtração para calcular o resultado.

def resto_divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    
    while a >= b:
        a -= b
    return a    