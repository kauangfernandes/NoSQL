from bs4 import BeautifulSoup

html = "<html><head><title>Meu Título</title></head><body></body></html>"
sopa = BeautifulSoup(html, 'html.parser')

titulo = sopa.find('title').text

print("Título da página:", titulo)