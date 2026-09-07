# Programa de cálculo de consumo de energia elétrica
# Autor: Caroline Tayar

# Entrada de dados
print("Programa de cálculo de consumo de energia elétrica")
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas_diarias = float(input("Digite o tempo médio de uso diário (em horas): "))

# Processamento de dados
# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_diarias * 30) / 1000
valor_kwh = 0.50

# Saída de dados
print("\nResultado do cálculo de consumo de energia elétrica:")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Valor estimado: R$ {consumo_mensal * valor_kwh:.2f}")