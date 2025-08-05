# Escreva um programa que solicita ao usuário a velocidade de um carro. Se a velocidade for superior a 80 km/h, o programa deve informar que o usuário foi multado e exibir o valor da multa. A multa custa R$ 5,00 por cada km/h acima do limite de 80 km/h.
velocidade = float(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print(f'Você foi multado por excesso de velocidade! Valor da multa: R$ {multa:.2f}')
if velocidade <= 80:
    print('Você está dentro do limite de velocidade. Não há multa.')    