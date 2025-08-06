# Exercício 4.16 - Corrija o programa abaixo:
# media = input("Digite sua média:")
# if media < 4:
#     print("Infelizmente você reprovou")
# if media < 7:
#     print("Você ficou de recuperação")
# if media > 7:
#     print("Você passou de ano")
media = float(input("Digite sua média:"))
if media < 4:
    print("Infelizmente você reprovou")
elif media >= 4 and media < 7:
    print("Você ficou de recuperação")
elif media >= 7 and media <= 10:
    print("Você passou de ano")
else:
    print("Média inválida! Por favor, insira uma média entre 0 e 10.")  