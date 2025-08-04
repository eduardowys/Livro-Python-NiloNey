# Exercício 3.15 – Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))  # Entrada da quantidade de cigarros fumados por dia
anos_fumando = int(input("Digite quantos anos você já fumou: "))  # Entrada da quantidade de anos fumando
minutos_perdidos_por_cigarro = 10  # Minutos perdidos por cada cigarro fumado
minutos_perdidos = cigarros_por_dia * minutos_perdidos_por_cigarro * 365 * anos_fumando  # Cálculo total de minutos perdidos
dias_perdidos = minutos_perdidos / (24 * 60)  # Conversão de minutos perdidos para dias perdidos
print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida devido ao fumo.")  # Exibe o total de dias perdidos