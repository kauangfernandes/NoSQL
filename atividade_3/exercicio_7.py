"""
Exercício 7: Criador de Iniciais
Crie uma função chamada iniciais que aceite um nome completo e retorne as iniciais de cada nome em letras maiúsculas. 
Por exemplo, para o nome "Maria Julia de Souza", a função deve retornar "M.J.S".
"""
def iniciais(nome):
    nomes = nome.strip()
    iniciais = [nome[0].upper() for nome in nomes]
    return ".".join(iniciais)

try:
    print("Ola, seja bem-vindo ao programa - Removendo Espaços Extras");
    ret = iniciais("Kauan Gomes Fernandes")
    print(ret);

except Exception as erro:
    print(f"Ocorreu problema interno :/");