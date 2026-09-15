"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:

nota1 = float(input("Digite a nota da primeira avaliação (peso 2 ): "))
nota2 = float(input("Digite a nota da segunda avaliação (peso 3): "))
nota3 = float(input("Digite a nota da terceira avaliação (peso 5): "))

# Calcule a média ponderada
peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
# Exiba a média final ponderada
print(f"A média final ponderada das avaliações é: {media_ponderada:.2f}")