"""
Exercício:
Calcular o custo total de uma refeição com gorjeta e
imposto.
Você receberá:
1) O preço base da refeição (meal_cost) — antes de gorjeta e
impostos.
2) A porcentagem da gorjeta (tip_percent).
3) A porcentagem do imposto (tax_percent).
Tarefas:
- Calcular o valor da gorjeta a partir do preço base.
- Calcular o valor do imposto a partir do preço base.
- Somar todos os valores para obter o custo total.
- Arredondar o valor final para o inteiro mais próximo.
- Mostrar o valor final.
Crie suas respostas abaixo de cada TODO
"""
# Entrada de dados
meal_cost = 12.00 # preço base da refeição
tip_percent = 20 # porcentagem da gorjeta
tax_percent = 8 # porcentagem do imposto

# TODO: Calcular gorjeta

gorjeta = meal_cost * (tip_percent/100)

# TODO: Calcular imposto

imposto = meal_cost * (tax_percent/100)

# TODO: Calcular total

custo_total = meal_cost + imposto + gorjeta

# TODO: Arredondar e exibir resultado

custo_total_arredondado = round(custo_total)
print(custo_total_arredondado)