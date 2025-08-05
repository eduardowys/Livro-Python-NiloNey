# Calculo imposto de renda
salario = float(input('Digite o salário do funcionário: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.30)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f'O imposto de renda a ser pago é: R$ {imposto:.2f}')
# Explicação: O programa calcula o imposto de renda com base no salário do funcionário.