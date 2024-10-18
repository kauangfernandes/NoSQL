"""
Exercício 3: Palíndromo Simples
Crie uma função chamada verificar_palindromo que receba uma string e 
verifique se ela é um palíndromo (a palavra é a mesma lida de frente para trás). 
A função deve ignorar letras maiúsculas e espaços.
"""

def verificar_palindromo(palavra=""):
    palavra = palavra.replace(" ", "").lower();
    palavra_invertida = palavra[::-1]

    if(palavra == palavra_invertida):
        return f"E um Palíndromo"
    else:
        return f"Não e um Palíndromo"


try:
    print("Ola, seja bem-vindo ao programa - Palíndromo Simples");
    ret = verificar_palindromo("Ana");
    print(ret);

except Exception as erro:
    print(f"Ocorreu problema interno :/");