"""
Exercício 2: Calculadora Simples
Crie uma função chamada calculadora que aceite três parâmetros: numero1, numero2 e operacao. 
A função deve executar a operação especificada ('+', '-', '*', '/') e retornar o resultado. 
Se a operação não for válida, retorne "Operação Inválida".

"""

def calculadora(numX=0, numY=0, op=""):

    if(op != "+" and op != "-" and op != "*" and op != "/"):
        return f"Operação Inválida"

    res = 0

    if op == "+":
        res = numX + numY;
        return res; 
            
    if op == "-":
        res = numX - numY;
        return res; 

    if op == "*":
        res = numX * numY;
        return res; 
            
    if op == "/":
        res = numX / numY;
        return res;

          

try:

    print("Ola, seja bem-vindo ao programa - Calculadora Simples");
    resultado = calculadora(10, 10, "+")
    print(resultado);
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");