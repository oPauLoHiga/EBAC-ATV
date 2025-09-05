import requests

response = requests.get('https://br.search.yahoo.com/')
print(response.text[:600])

#comit teste