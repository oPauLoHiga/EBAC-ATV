#https://dados.gov.br/home
#https://br.search.yahoo.com/
#https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-02-2024/tabelas.html

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("******  requests  *******")
response = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-02-2024/tabelas.html')
print(response.text[:600])

print("****** BeautifulSoup *******")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print("****** Pandas *******")
url_dados = (pd.read_html('https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-02-2024/tabelas.html'))
print(url_dados[0])