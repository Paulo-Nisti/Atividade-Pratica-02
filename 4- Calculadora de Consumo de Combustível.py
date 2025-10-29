# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# Distância percorrida: 300 km
# Combustível gasto: 25 litros 

# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

# 1. Definição dos dados da viagem
distancia_percorrida = 300  # em quilômetros
combustivel_gasto = 25      # em litros

# 2. Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# 3. Exibição do relatório completo
print("--- Relatório de Consumo de Combustível ---")
print(f"Distância Total Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("---------------------------------------------")
print(f"Consumo Médio do Veículo: {consumo_medio:.2f} km/l")