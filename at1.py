def calcular_salario(salario_fixo, comissao_por_carro, valor_total_vendas, num_carros_vendidos):
    # Calcula comissão de 5% sobre o valor total de vendas
    percentual_vendas = 0.05 * valor_total_vendas if num_carros_vendidos > 0 else 0
    # Calcula bônus adicional de 10% caso o vendedor tenha vendido mais de 10 carros
    bonus = 0.10 * valor_total_vendas if num_carros_vendidos > 10 else 0
    # Calcula a comissão fixa por carro vendido
    comissao_total = num_carros_vendidos * comissao_por_carro if num_carros_vendidos > 0 else 0
    
    # Calcula o salário final
    salario_final = salario_fixo + comissao_total + percentual_vendas + bonus
    return salario_final

# Exemplo de uso:
salario_fixo = 2000         # Exemplo de salário fixo
comissao_por_carro = 150    # Exemplo de comissão por carro vendido
valor_total_vendas = 50000  # Exemplo de valor total de vendas
num_carros_vendidos = 12    # Exemplo de número de carros vendidos

salario = calcular_salario(salario_fixo, comissao_por_carro, valor_total_vendas, num_carros_vendidos)
print(f"Salário final do vendedor: R$ {salario:.2f}")
