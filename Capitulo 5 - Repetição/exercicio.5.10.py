# Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta {questao} (A, B, C ou D): ")
    if questao == 1 and resposta == 'B':
        pontos += 1
    if questao == 2 and resposta == 'C':
        pontos += 1
    if questao == 3 and resposta == 'D':
        pontos += 1
    questao += 1
print(f"Você obteve {pontos} pontos.")