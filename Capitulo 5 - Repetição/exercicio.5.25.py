# Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b = 2. Calcule p usando a fórmula p = (b + (n / b)) / 2. Agora, calcule o quadrado de p. A cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.
n = float(input("Digite um número para calcular a raiz quadrada: "))
b = n / 2  # Inicializa b com metade do número  
while True:
    p = (b + (n / b)) / 2  # Calcula p usando a fórmula
    quadrado_p = p ** 2  # Calcula o quadrado de p
    if abs(n - quadrado_p) < 0.0001:  # Verifica a condição de parada
        break
    b = p  # Atualiza b para o próximo passo
print(f"A raiz quadrada aproximada de {n} é {p:.4f}.")  
