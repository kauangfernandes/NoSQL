
msg = "";

try:
    nome = input("Digite seu nome: ");
except Exception as erro:
    print("Ocoreu erro interno tente novamente mais tarde :)");

try:
    idade = int(input("Digite sua idade: "));
except Exception as erro:
    print("Ocoreu erro interno tente novamente mais tarde :)");

try:
    if(idade < 18):
        msg = "menor de idade :)";
    else:
        msg = "maior de idade :)";

    print(f"Ola {nome} voce tem {idade} ou seja voce e {msg}");

except Exception as erro:
    print("Ocoreu erro interno tente novamente mais tarde :)");


try:
    if(idade >= 18):
        print("Seja bem vindo a Sessao :)");


except Exception as erro:
    print("Ocoreu erro interno tente novamente mais tarde :)");