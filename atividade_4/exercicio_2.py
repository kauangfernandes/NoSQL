"""
Função Lambda:

Escreva uma função lambda que eleve um número ao quadrado.

Explicação: Ensina a praticidade das lambdas para funções de uma linha, ajudando na compreensão de expressões simples.
"""

def Lambda(num):
    return num * num

try:

    print("Ola, seja bem-vindo ao programa - Função Lambda");
    ret = Lambda(3)
    print(f"Resultado e: {ret}");
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");