# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
total = 0
count = 0
while True:
    v = int(input("Digite um número inteiro (0 para sair): "))
    if v == 0:
        break  
    total += v
    count += 1
media = total / count
print(f"Quantidade de números digitados: {count}")
print(f"Soma dos números: {total}")
print(f"Média aritmética: {media:.2f}")