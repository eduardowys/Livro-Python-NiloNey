# O programa verifica se um aluno foi aprovado com base nas notas de 3 matérias.
# Para ser aprovado, o aluno precisa ter nota maior ou igual a 7 em todas as matérias.
"""
materia1 = float(input("Digite a nota da matéria 1: ")) # Entrada da nota da matéria 1, convertida para float
materia2 = float(input("Digite a nota da matéria 2: ")) # Entrada da nota da matéria 2, convertida para float
materia3 = float(input("Digite a nota da matéria 3: ")) # Entrada da nota da matéria 3, convertida para float
aprovado = materia1 >= 7 and materia2 >= 7 and materia3 >= 7    # Verifica se o aluno foi aprovado: todas as notas devem ser >= 7

# Exibe True ou False informando se o aluno foi aprovado
print("Aluno aprovado:", aprovado)  

# Exibe as notas com 2 casas decimais usando f-string
print(f"Notas: Matéria 1: {materia1:.2f}, Matéria 2: {materia2:.2f}, Matéria 3: {materia3:.2f}")

# Exibe as notas com diferentes alinhamentos e 2 casas decimais usando .format()
print("Notas: Matéria 1: {:3}, Matéria 2: {:.2f}, Matéria 3: {:<3}".format(materia1, materia2, materia3))

# Exibe as notas com formatação do estilo antigo (%) — corrigido com uso consistente de casas decimais
print("Notas: Matéria 1: %.2f, Matéria 2: %.2f, Matéria 3: %.2f" % (materia1, materia2, materia3))
"""

# Fatiamento de string python
string = "ABCDE"
print("Fatiamento de string:", string[1:4])  # Exibe os caracteres do índice 1 ao 3,obs: o índice 4 não é incluído
print("Fatiamento de string do início ao índice 3:", string[:3]) # Exibe os caracteres do início até o índice 2
print("Fatiamento de string do índice 2 ao fim:", string[2:])  # Exibe os caracteres do índice 2 até o final
print("Fatiamento de string com passo:", string[1:4:2])  # Exibe os caracteres do índice 1 ao 3 com passo 2
print("Fatiamento de string do início ao fim:", string[:])  # Exibe toda a string
print("Fatiamento de string com passo negativo:", string[::-1])  # Exibe a string invertida
print("Fatiamento de string com passo negativo do índice 3 ao início:", string[3::-1])  # Exibe os caracteres do índice 3 até o início, invertendo a ordem
print("Fatiamento de string com passo:", string[::2])  # Exibe os caracteres com passo 2        
