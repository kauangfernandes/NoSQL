"""
Crie uma função que receba o nome e a idade de uma pessoa e retorne uma saudação que inclua a idade.
Explicação: Este exercício ajuda os alunos a aplicar o conceito de parâmetros e retorno em funções.
"""

def saudar(nome="", idade=0):
    return f"{saudacao}, {nome}. Sua idade e {idade}."

try:

    print("Ola, seja bem-vindo ao programa - Saudação Personalizada");
    saudacao = saudar(nome="Kauan", idade=21)
    print(saudacao);
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");