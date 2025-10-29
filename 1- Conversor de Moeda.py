# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60 
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.


# 1. Definição dos valores iniciais
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# 2. Cálculo das conversões
valor_em_dolares = valor_reais / taxa_dolar
valor_em_euros = valor_reais / taxa_euro

# 3. Exibição dos resultados formatados
print("--- Conversão de Moeda ---")
print(f"Valor original em Reais: R$ {valor_reais:.2f}\n") # \n para pular uma linha

print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro:  R$ {taxa_euro:.2f}")
print("----------------------------")

# Exibe os valores convertidos e arredondados para duas casas decimais
print(f"Valor convertido em Dólares: US$ {valor_em_dolares:.2f}")
print(f"Valor convertido em Euros:   € {valor_em_euros:.2f}")