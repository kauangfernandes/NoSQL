"""
Exercício 6 - Calculadora de IMC
Conteúdo:
Descrição:
Escreva um programa que peça ao usuário seu peso (em kg) e sua altura (em metros).
O programa deve calcular o Índice de Massa Corporal (IMC) e imprimir o resultado.
Fórmula do IMC: IMC=peso sobre altura ao quadrado.
"""

try:

    print("Ola, seja bem-vindo ao programa - Calculadora de IMC");
    
    while True:

        while True:
            try:
                altura = float(input("Qual e altura em (Metros): "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        while True:
            try:
                peso = float(input("Qual e o peso em (KG) "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");

        imc =  peso / (altura * altura);

        print(f"O IMC e {imc}");

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");