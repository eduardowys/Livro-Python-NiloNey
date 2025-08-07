# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:
"""
Código | Preço
   1   | 0,50
   2   | 1,00
   3   | 4,00
   5   | 7,00
   6   | 8,00
"""
total = 0
while True:
   cod = int(input("Digite o código do produto (0 para finalizar): "))
   if cod == 0:
      print("Finalizando a compra...")
      break
   quant = int(input("Digite a quantidade comprada: "))
   if cod == 1:
      total += 0.50 * quant
   if cod == 2:
      total += 1.00 * quant
   if cod == 3:
      total += 4.00 * quant
   if cod == 5:
      total += 7.00 * quant
   if cod == 6:
      total += 8.00 * quant
print(f"Total a pagar: R$ {total:.2f}")