# Exercício 4.15 - Reescreva o programa abaixo com if-elif-else:
# hora = int(input("Digite a hora atual:"))
# if hora < 12:
#     print("Bom dia!")
# if hora >= 12 and hora <= 18:
#     print("Boa tarde!")
# if hora >= 18:
#     print("Boa noite!")
hora = int(input("Digite a hora atual:"))
if hora < 12:
    print("Bom dia!")
elif hora >= 12 and hora <= 18:
    print("Boa tarde!")
elif hora > 18 and hora <= 23:
    print("Boa noite!")
else:
    print("Hora inválida! Por favor, insira uma hora entre 0 e 23.")