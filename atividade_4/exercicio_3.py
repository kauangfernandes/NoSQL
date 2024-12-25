"""
Listas:
Crie uma lista de cinco números inteiros e calcule a soma dos elementos.
Explicação: Exercício prático para demonstrar a manipulação de listas e a soma de seus elementos.
"""



try:

    print("Ola, seja bem-vindo ao programa - Listas");
    numeros = [1, 2, 3, 4, 5]
    soma = sum(numeros)
    print("A soma dos números é:", soma)
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");