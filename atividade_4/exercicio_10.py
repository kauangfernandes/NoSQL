class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("João", 30)

# Chamando o método apresentar() para cada objeto
pessoa1.apresentar()
pessoa2.apresentar()


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        print(f"Este carro é um {self.marca} {self.modelo}, ano {self.ano}.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Chamando o método descricao()
meu_carro.descricao()

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

# Criando uma conta bancária
minha_conta = ContaBancaria("João Silva", 1000)

# Realizando um depósito
minha_conta.depositar(500)

# Tentando sacar um valor maior que o saldo
minha_conta.sacar(1600)

# Realizando um saque válido
minha_conta.sacar(300)