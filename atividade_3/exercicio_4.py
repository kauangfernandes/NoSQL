"""
Exercício 4: Contador de Vogais
Crie uma função chamada contar_vogais que receba uma string e conte quantas 
vogais (a, e, i, o, u) existem nela. A função deve retornar a quantidade total de vogais.
"""

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador


try:

    print("Ola, seja bem-vindo ao programa - Contador de Vogais");
    ret = contar_vogais("Kauan");
    print(ret);
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");