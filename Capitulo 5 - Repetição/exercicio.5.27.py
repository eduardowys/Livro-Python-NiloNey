# Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501.
numero = input("Digite um número: ")
numero_invertido = numero[::-1]  # Inverte os dígitos do número 
if numero == numero_invertido:
    print(f"{numero} é um palíndromo.")
else:
    print(f"{numero} não é um palíndromo.") 
    