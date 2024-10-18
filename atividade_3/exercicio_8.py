"""
Exercício 8: Reverter String
Crie uma função chamada reverter_string que receba uma string e retorne a mesma string, mas com a ordem dos caracteres invertida.
"""
def reverter_string(texto):
  return texto[::-1]


try:
    print("Ola, seja bem-vindo ao programa - Removendo Espaços Extras");
    ret = reverter_string("Kauan")
    print(ret);

except Exception as erro:
    print(f"Ocorreu problema interno :/");