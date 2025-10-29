# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# Nome do produto: "Camiseta"
# Preço original: R$ 50.00

# Porcentagem de desconto: 20% 
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

# 1. Definição das informações do produto e do desconto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# 2. Cálculo do valor do desconto
# Para calcular a porcentagem, dividimos o percentual por 100
valor_do_desconto = preco_original * (percentual_desconto / 100)

# 3. Cálculo do preço final
preco_final = preco_original - valor_do_desconto

# 4. Exibição de todos os detalhes
print("--- Cálculo de Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto Aplicado: {percentual_desconto}%")
print("---------------------------")
print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")