"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_consumido = float(input("Digite o valor total consumido no restaurante em R$: "))
taxa_servico = 0.10
valor_final = valor_consumido * (1 + taxa_servico)
print(f"O valor final da conta a pagar, incluindo a taxa de 10% de serviço é: R$ {valor_final:.2f}")