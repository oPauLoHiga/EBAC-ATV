import requests
from bs4 import BeautifulSoup

response = requests.get('https://br.search.yahoo.com/')
print(response.text[:600])

soup = BeautifulSoup()