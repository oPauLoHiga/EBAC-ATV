#"C:/Users/paulo/OneDrive/Documentos/teste de texto.txt"
import requests

def enviar_arquivo(url):
    caminho = 'C:/Users/paulo/OneDrive/Documentos/teste de texto.txt'

    #enviar o arquivo
    requisicao = requests.post('https://gofile.io/home', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado. Link para acesso: ",url)