"""
Exercício 6: Removendo Espaços Extras
Crie uma função chamada remover_espacos que receba uma frase com espaços 
em excesso no início e no fim e retorne a frase corrigida. Utilize o método strip().
"""

def remover_espacos(texto):
    texto = texto.strip()
    return texto

try:
    print("Ola, seja bem-vindo ao programa - Removendo Espaços Extras");
    ret = remover_espacos("  Hello World!  ")
    print(ret);

except Exception as erro:
    print(f"Ocorreu problema interno :/");