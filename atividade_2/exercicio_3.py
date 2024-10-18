"""
Exercício 3 - Verificação de Paridade
Conteúdo:
Descrição:
Escreva um programa que peça ao usuário um número inteiro.
O programa deve verificar se o número é par ou ímpar e imprimir uma mensagem apropriada.
"""

try:

    print("Ola, seja bem-vindo ao programa - Verificação de Paridade");
    
    while True:

        while True:
            try:
                num = int(input("Digite um numero interio: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        if num % 2 == 0:
            print("O numero digitado e PAR");    
        else:
            print("O numero digitado e Impra");
        

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");