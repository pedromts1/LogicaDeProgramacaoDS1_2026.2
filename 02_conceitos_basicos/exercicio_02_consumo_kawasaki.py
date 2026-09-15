"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

distancia = float(input("Digite a distancia total percorrida (KM): "))

combustivel = float(input("Digite o valor total gasto (litros): "))

if combustivel > 0:
    consumo = distancia / combustivel

    print(f"\nO consumo medio da motocicleta foi de {consumo:.2f} KM/L.")

else:
    print("\nNao e possivel calcular o consumo sem combustivel.")