#https://dados.gov.br/home
#https://br.search.yahoo.com/

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("******  requests  *******")
response = requests.get('https://dados.gov.br/home')
print(response.text[:600])

print("****** BeautifulSoup *******")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])