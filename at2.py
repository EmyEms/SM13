def calcular_soma_produto(idade_h1, idade_h2, idade_m1, idade_m2):
    # Validação de entrada
    for idade in [idade_h1, idade_h2, idade_m1, idade_m2]:
        if not isinstance(idade, int) or idade <= 0:
            return "Erro: Todas as idades devem ser números inteiros positivos."

    # Determina o homem mais velho e o homem mais novo
    homem_mais_velho = max(idade_h1, idade_h2)
    homem_mais_novo = min(idade_h1, idade_h2)

    # Determina a mulher mais velha e a mulher mais nova
    mulher_mais_velha = max(idade_m1, idade_m2)
    mulher_mais_nova = min(idade_m1, idade_m2)

    # Calcula a soma e o produto de acordo com as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return {
        "Soma (homem mais velho + mulher mais nova)": soma,
        "Produto (homem mais novo * mulher mais velha)": produto
    }

# Exemplo de uso:
idade_h1 = 25  # Idade do primeiro homem
idade_h2 = 30  # Idade do segundo homem
idade_m1 = 20  # Idade da primeira mulher
idade_m2 = 35  # Idade da segunda mulher

resultado = calcular_soma_produto(idade_h1, idade_h2, idade_m1, idade_m2)
print(resultado)
