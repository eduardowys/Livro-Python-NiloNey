# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão 
# de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. 
# Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
num1 = int(input("Digite o primeiro número (dividendo): "))
num2 = int(input("Digite o segundo número (divisor): "))
quociente = 0
resto = num1    
while resto >= num2:
    resto -= num2
    quociente += 1  
print(f"A divisão inteira de {num1} por {num2} é {quociente} e o resto é {resto}.")

