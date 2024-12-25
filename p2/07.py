numeros = [2, 4, 6, 8]
valor = int(input("Digite o valor desejado: "))

resultado = []

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] + numeros[j] == valor:
            resultado.append((numeros[i], numeros[j]))

print("Números encontrados:", resultado)