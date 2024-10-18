"""
Exercício 1: Saudação Personalizada
Crie uma função chamada saudar_usuario que receba como parâmetros o nome e a 
idade de um usuário e retorne uma mensagem como: "Olá, João! Você tem 25 anos.".
"""

def saudar(nome="", idade=0, saudacao="Olá"):
    return f"{saudacao}, {nome}. Sua idade e {idade}."

try:

    print("Ola, seja bem-vindo ao programa - Saudação Personalizada");
    saudacao = saudar(nome="Kauan", idade=21)
    print(saudacao);
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");