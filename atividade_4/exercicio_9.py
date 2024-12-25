"""
Usando o módulo math, crie um programa que peça ao usuário para digitar um número e exiba a raiz quadrada desse número.
    
Dica: Importe a função sqrt do módulo math.
  
Exercício 2: Crie um módulo chamado meu_modulo.py e adicione uma função chamada saudacao que exibe “Olá, bem-vindo ao meu módulo!”. Em outro arquivo Python, importe e execute essa função.
    
Dica: Use from meu_modulo import saudacao.
  
Exercício 3: Crie um pacote chamado calculadora que contenha dois módulos: operacoes_basicas.py (com funções de soma e subtração) e operacoes_avancadas.py (com funções de multiplicação e divisão). Em um arquivo principal, importe os módulos e execute uma operação de cada um.
    
Dica: Estrutura do pacote:
    
calculadora/
  
├── __init__.py
  
├── operacoes_basicas.py
  
└── operacoes_avancadas.py
"""

try:
    import math
    numero = float(input("Digite um número: "))
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é:", raiz_quadrada)
    
    from meu_modulo import saudacao
    saudacao()
    
    
    from calculadora import soma, subtracao
    from calculadora import multiplicacao, divisao

    resultado_soma = soma(5, 3)
    resultado_subtracao = subtracao(10, 4)
    resultado_multiplicacao = multiplicacao(2, 6)
    resultado_divisao = divisao(15, 3)

    print(resultado_soma)
    print(resultado_subtracao)
    print(resultado_multiplicacao)
    print(resultado_divisao)
    
    

except Exception as erro:
        print(f"Ocorreu problema interno :/");