"""
Use compreensão de lista para criar uma lista que contenha os quadrados de números de 1 a 10.
    
Saída Esperada: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  
Exercício 2: Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que têm mais de 4 letras.
    
Exemplo: palavras = ["casa", "python", "aula", "exemplo", "lista"]
  
Saída Esperada: ["python", "exemplo", "lista"]
  
Exercício 3: Dada uma lista de números, crie uma nova lista que contenha apenas os números pares ao quadrado.
    
Exemplo: numeros = [1, 2, 3, 4, 5, 6]
  
Saída Esperada: [4, 16, 36]
"""

try:
    quadrados = [x**2 for x in range(1, 11)]
    print(quadrados)  # Saída: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    palavras = ["casa", "python", "aula", "exemplo", "lista"]
    palavras_longas = [palavra for palavra in palavras if len(palavra) > 4]
    print(palavras_longas)  # Saída: ['python', 'exemplo', 'lista']
    
    numeros = [1, 2, 3, 4, 5, 6]
    quadrados_pares = [num**2 for num in numeros if num % 2 == 0]
    print(quadrados_pares)  # Saída: [4, 16, 36]
    
    

except Exception as erro:
        print(f"Ocorreu problema interno :/");