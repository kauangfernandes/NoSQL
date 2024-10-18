"""
Exercício 5: Fatiamento de Nomes
Crie uma função chamada fatiar_nome que receba um nome completo e retorne:
"""

def fatiar_nome(nome_completo):
  nomes = nome_completo.split()
  primeiro_nome = nomes[0]
  ultimo_nome = nomes[-1]

  return primeiro_nome, ultimo_nome

try:
    print("Ola, seja bem-vindo ao programa - Contador de Vogais");
    nome, ultimo = fatiar_nome("Kauan Gomes Fernandes");
    print(f"Primeiro nome: {nome}\nÚltimo nome: {ultimo}")

    

except Exception as erro:
    print(f"Ocorreu problema interno :/");