# Exercício 4.11 - Aprove ou negue um empréstimo para compra de casa. Pergunte valor da casa, salário e anos para pagar. Prestação mensal não pode exceder 30% do salário. Prestação = valor da casa / (anos * 12).
casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos deseja pagar: "))
prestacao = casa / (anos * 12)
if prestacao <= salario * 0.3:
    print(f"Empréstimo aprovado! A prestação mensal será de R${prestacao:.2f}.")
else:
    print(f"Empréstimo negado! A prestação mensal de R${prestacao:.2f} excede 30% do seu salário de R${salario:.2f}.")
    