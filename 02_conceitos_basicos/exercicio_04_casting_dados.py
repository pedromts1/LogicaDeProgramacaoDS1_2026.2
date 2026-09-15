"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:

ano_nascimento_str = input("Digite o seu ano de nascimento: ")
# Convertendo a entrada de texto para inteiro
ano_nascimento = int(ano_nascimento_str)
# Calculando a idade em 2026
idade_em_2026 = 2026 - ano_nascimento
# Exibindo a idade com uma mensagem personalizada
print(f"Você terá {idade_em_2026} anos até o final de 2026.")