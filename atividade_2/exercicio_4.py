"""
Exercício 4
Escreva um programa que peça ao usuário dois números e uma operação (soma, subtração, multiplicação, divisão).
O programa deve realizar a operação e imprimir o resultado.
"""

try:

    print("Ola, seja bem-vindo ao programa.");
    
    while True:

        while True:
            try:
                p = float(input("Digite o primeiro valor: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        while True:
            try:
                s = float(input("Digite o segundo valor: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");
        
        while True:
            try:
                print("Escolha uma operacao:\n1 - para soma\n2 - para subtração\n3 - multiplicação\n4 - para divisão");
                op = int(input("Opcao: "));
                break

            except Exception as erro:
                print("Digite um valor valido :)");

        def operacao(p_num, s_num, op):
            res = 0

            if op == 1:
                res = p_num + s_num;
            
            if op == 2:
                res = p_num - s_num;

            if op == 3:
                res = p_num * s_num;
            
            if op == 4:
                res = p_num / s_num;

            return res;        

        res = operacao(p, s, op)

        print(f"------------------------------\nO resultado da operacao e: {res}\n------------------------------");




        condicao = str(input("\nDidite S - para Sim e N - para Nao e \npressione ENTER para confimar\nOpcao: "));
        if condicao == "n" or condicao == "Nao" or condicao == "0":
            print("Obrigado por usar :)");
            break


except Exception as erro:
    print(f"Ocorreu problema interno :/ {erro}");




