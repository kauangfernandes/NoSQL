import os

# Criar diretório
diretorio = "Relatórios"
os.mkdir(diretorio)
print("Diretório criado!")

# Listar arquivos
arquivos = os.listdir(diretorio)
print("Arquivos no diretório:", arquivos)