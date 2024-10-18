"""
Exercício 7
Soma de números pares:
Crie uma função que recebe uma lista de números e retorna a soma dos números pares usando um laço for.
"""

try:

    print("Ola, seja bem-vindo ao programa - Cálculo de Área de Retângulo");
    
    while True:

        def soma_pares(lista):
            soma = 0

            for numero in lista:
                if numero % 2 == 0:
                    soma = soma + numero

            return soma

        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        resultado = soma_pares(lista)
        print("A soma dos números pares é:", resultado)

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");