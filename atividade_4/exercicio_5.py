"""
Manipulação de Arquivos:
  
Crie um arquivo alunos.txt e escreva o nome de cinco alunos, um por linha. Depois, abra e exiba o conteúdo.
  
Explicação: Desenvolve a prática de leitura e escrita de arquivos, habilidades essenciais para manipulação de dados externos.
"""



try:

    print("Ola, seja bem-vindo ao programa - Manipulação de Arquivos:");

    """
        CASO O AQUIVO NAO EXISTA E CRIADO.
    """
    arquivo =  open("alunos.txt", "w")

    arquivo.write('Alice\n')
    arquivo.write('Bob\n')
    arquivo.write('Charlie\n')
    arquivo.write('David\n')
    arquivo.write('Eva\n')


    arquivo =  open("alunos.txt", "r")

    #print(arquivo.readline())
    linhas = arquivo.readlines()


    for linha in linhas:
        print(f"Aluno: {linha}")

    arquivo.close()


except Exception as erro:
    print(f"Ocorreu problema interno :/");