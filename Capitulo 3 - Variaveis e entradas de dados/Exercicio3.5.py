#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagar imposto pessoas cujo salário é maior que 1.200.
salario = float(input("Digite o salário da pessoa: "))
deve_pagar_imposto = salario > 1200
print("Deve pagar imposto:", deve_pagar_imposto)