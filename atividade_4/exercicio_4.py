"""
Dicionários:
Crie um dicionário que contenha informações sobre um carro (marca, modelo, ano) e imprima uma frase com esses dados. 
Explicação: Demonstra como armazenar e acessar dados em dicionários.
"""



try:

    print("Ola, seja bem-vindo ao programa - Dicionários");
    carro = {
        "marca": "Volkswagen",
        "modelo": "Gol",
        "ano": 2023
    }

    print(f"Meu carro é um {carro['marca']} {carro['modelo']} {carro['ano']}.")
    

except Exception as erro:
    print(f"Ocorreu problema interno :/");