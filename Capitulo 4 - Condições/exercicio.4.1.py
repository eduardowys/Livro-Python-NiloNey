# Analise o programa 4.1 Responda o que acontece se o primeiro e o segundo valor forem iguais? Expliquem
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('O primeiro valor é maior que o segundo valor.')
if a < b:
    print('O segundo valor é maior que o primeiro valor.')  
# Explicação: Se o primeiro e o segundo valor forem iguais, nenhum dos blocos de código dentro das condições if será executado, e nada será impresso na tela. Portanto, não haverá saída visível para o usuário. Isso ocorre porque as condições a > b e a < b não são satisfeitas quando os valores são iguais.
# Assim, o programa não informa nada sobre a relação entre os dois valores quando eles são iguais