#https://python.org.br/web/

import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#exibi o texto
# print(extracao.text.strip())

#Filtrar a exibição pela tag
# for link_texto in extracao.find_all('h2'):
#     titulo = link_texto.text.strip()
#     print("titulo: ", titulo)

#Contar qtd de tutilo e paragrafro
# contar_titulos = 0
# contar_paragrafo = 0
#
# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name == 'h2':
#         contar_titulos += 1
#     elif linha_texto.name == 'p':
#         contar_paragrafo += 1
#
# print('Total de titulos: ',contar_titulos)
# print('Total de paragrafos: ',contar_paragrafo)

#exebir o texto h2 e p
# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print('Titulo:\n ',titulo)
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo:\n ',paragrafo)

#exibir tags aninhada
for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), '| URL:', a['href'])