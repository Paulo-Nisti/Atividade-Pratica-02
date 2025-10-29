# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5 
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

# 1. Definição das notas do aluno
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# 2. Cálculo da média
# A média é a soma das notas dividida pela quantidade de notas
soma_das_notas = nota1 + nota2 + nota3
media_final = soma_das_notas / 3

# 3. Exibição das notas e do resultado final
print("--- Cálculo da Média Escolar ---")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("--------------------------------")
print(f"Média Final: {media_final:.2f}")
