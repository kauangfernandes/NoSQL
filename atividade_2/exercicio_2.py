""" Exercício 2 - Cálculo de Área de Retângulo
Conteúdo:
Descrição:
Escreva um programa que peça ao usuário a largura e a altura de um retângulo.
O programa deve calcular e imprimir a área do retângulo.
"""
try:

    print("Ola, seja bem-vindo ao programa - Cálculo de Área de Retângulo");
    
    while True:

        while True:
            try:
                altura = float(input("Qual e altura do seu ratangulo: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        while True:
            try:
                base = float(input("Qual e a base do seu ratangulo: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");

        area = altura * base;

        print(f"A area do retangulo e {area}");

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");