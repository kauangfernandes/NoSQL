"""
Crie um programa que peça ao usuário para digitar dois números e, em seguida, 
divida o primeiro pelo segundo. Adicione tratamento de exceção para garantir
 que o programa não quebre se o usuário inserir zero no segundo número.    
Dica: Use try e except ZeroDivisionError.
"""



try:

    while True:

        while True:
            try:
                x = int(input("Digite o primeiro numero: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        while True:
            try:
                y = int(input("Digite o segundo valor: "));
            
                if(y != 0):
                    break

            except ZeroDivisionError as erro:
                print("Digite um valor valido :)");

        divisao = x / y;

        print(f"O resultado e: {divisao}");

        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));

        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/");