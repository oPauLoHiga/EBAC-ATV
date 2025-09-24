#C:/Users/paulo/Downloads/produtos_informatica.xlsx
import requests

def enviar_arquivo():
    caminho = 'C:/Users/paulo/Downloads/produtos_informatica.xlsx'

    #enviar o arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso: ",url)

def receber_arquivo(file_url):
    #Receber o arquivo
    requisicao = requests.get(file_url)

    #Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso!')
    else:
        print("Erro ao baixar o arquivo: ", requisicao.json())

enviar_arquivo() #recebe o link pra colocar no #recever_arquivo
#receber_arquivo('')