import requests

url = "https://api.agify.io?name=kauan"
resposta = requests.get(url)  # Aqui realizamos a requisição GET à API

if resposta.status_code == 200:
    dados = resposta.json()
    print("Idade estimada:", dados['age'])
else:
    print("Erro na requisição.")