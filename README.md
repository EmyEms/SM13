
# Atividades de Cálculo de Salário e Idades

Este repositório contém duas atividades de programação em Python para cálculo de salário e manipulação de idades com base em regras específicas de negócios.

## Atividade 1: Cálculo do Salário de Vendedores em uma Revendedora de Carros

### Descrição

Este programa calcula o salário final de um vendedor em uma revendedora de carros, levando em consideração o salário fixo, uma comissão fixa por cada carro vendido e um percentual sobre o valor total de vendas. Há também um bônus adicional para vendedores que superam uma meta de vendas.

### Regras de Negócio

1. **Salário fixo**: Cada vendedor recebe um valor fixo mensal.
2. **Comissão fixa por carro**: O vendedor ganha uma quantia adicional para cada carro vendido.
3. **Percentual sobre vendas**: O vendedor recebe 5% sobre o total das suas vendas.
4. **Bônus**: Se o vendedor vender mais de 10 carros, ele recebe um bônus de 10% sobre o total das vendas.

### Casos de Pagamento

| Condição                | Salário Fixo (S) | Comissão Fixa (F) | 5% sobre Vendas (P) | Bônus 10% sobre Vendas (B) | Salário Final                                                   |
|-------------------------|------------------|--------------------|----------------------|-----------------------------|------------------------------------------------------------------|
| Nenhum carro vendido    | Sim              | Não               | Não                 | Não                          | \( S \)                                                          |
| Entre 1 e 10 carros     | Sim              | Sim               | Sim                 | Não                          | \( S + (C \times F) + (0.05 \times V) \)                         |
| Mais de 10 carros       | Sim              | Sim               | Sim                 | Sim                          | \( S + (C \times F) + (0.05 \times V) + (0.10 \times V) \)       |

### Exemplo de Uso

```python
salario_fixo = 2000         # Salário fixo
comissao_por_carro = 150    # Comissão por carro vendido
valor_total_vendas = 50000  # Valor total das vendas
num_carros_vendidos = 12    # Número de carros vendidos

salario_final = calcular_salario(salario_fixo, comissao_por_carro, valor_total_vendas, num_carros_vendidos)
print(f"Salário final do vendedor: R$ {salario_final:.2f}")
```

---

## Atividade 2: Cálculo de Idades - Soma e Produto entre Homens e Mulheres

### Descrição

Este programa lê as idades de dois homens e duas mulheres e realiza cálculos com base em regras de um estudo antropológico. A idade do homem mais velho é somada à idade da mulher mais nova, enquanto a idade do homem mais novo é multiplicada pela idade da mulher mais velha.

### Regras de Negócio

1. O programa identifica o homem mais velho e o homem mais novo, assim como a mulher mais velha e a mais nova.
2. A idade do homem mais velho é somada à idade da mulher mais nova.
3. A idade do homem mais novo é multiplicada pela idade da mulher mais velha.

### Tabela-Verdade para Identificação das Idades

| Idade Homem 1 | Idade Homem 2 | Idade Mulher 1 | Idade Mulher 2 | Homem Mais Velho | Homem Mais Novo | Mulher Mais Velha | Mulher Mais Nova |
|---------------|---------------|----------------|----------------|-------------------|-----------------|-------------------|------------------|
| 25            | 30            | 20            | 35            | 30               | 25              | 35               | 20              |
| 40            | 35            | 28            | 22            | 40               | 35              | 28               | 22              |
| 33            | 33            | 19            | 21            | 33               | 33              | 21               | 19              |
| 50            | 45            | 30            | 30            | 50               | 45              | 30               | 30              |

### Exemplo de Uso

```python
idade_h1 = 25  # Idade do primeiro homem
idade_h2 = 30  # Idade do segundo homem
idade_m1 = 20  # Idade da primeira mulher
idade_m2 = 35  # Idade da segunda mulher

resultado = calcular_soma_produto(idade_h1, idade_h2, idade_m1, idade_m2)
print(resultado)
```

---

## Estrutura dos Arquivos

- **atividade1_salario.py**: Código para a atividade de cálculo de salário.
- **atividade2_idades.py**: Código para a atividade de cálculo de idades.



