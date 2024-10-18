"""
Exercício 5 - Conversão de Temperatura
Conteúdo:
Descrição:
Escreva um programa que peça ao usuário uma temperatura em graus Celsius.
O programa deve converter a temperatura para Fahrenheit e imprimir o resultado.
Fórmula de conversão: 𝐹=9/5𝐶+32F=59C+32

"""

try:

    print("Ola, seja bem-vindo ao programa - Conversão de Temperatura");
    
    while True:

        while True:
            try:
                celsius = float(input("Qual a temperatura em celsius: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        fahrenheit = (celsius * 9/5) + 32
        
        print(f"A consercao de graus CELSIUS {celsius} para Fahrenheit e igual a: {fahrenheit} ");

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");