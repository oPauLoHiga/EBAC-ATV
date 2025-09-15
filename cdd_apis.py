#"C:/Users/paulo/OneDrive/Documentos/teste de texto.txt"
import requests

def enviar_arquivo():
    caminho = 'C:/Users/paulo/OneDrive/Documentos/teste de texto.txt'

    #enviar o arquivo
    requisicao = requests.post('https://api.gofile.io/v2/upload', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado. Link para acesso: ",url)

def receber_arquivo(file_url):
    #Receber o arquivo
    requisicao = requests.get(file_url)

    #Salvar o arquivo
    if requisicao.ok:
        with open('teste de texto.txt', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso!')
    else:
        print("Erro ao baixar o arquivo: ", requisicao.json())

enviar_arquivo()
#receber_arquivo()