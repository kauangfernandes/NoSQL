"""
Crie um programa que peça ao usuário para abrir um arquivo (use input() para obter o nome do arquivo). 
Use try para tentar abrir o arquivo e exiba uma mensagem de erro apropriada se o arquivo não for encontrado.
"""

nome = input("Digite o nome do arquivo: ")

try:
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read();
        print(conteudo)

except Exception as erro:
        print(f"Ocorreu problema interno :/");