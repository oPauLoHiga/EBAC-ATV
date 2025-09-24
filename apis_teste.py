import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def upload_e_baixar_gofile(token, caminho_arquivo):
    # --- UPLOAD VIA API ---
    url_upload = "https://upload.gofile.io/uploadfile"
    headers = {"Authorization": f"Bearer {token}"}

    with open(caminho_arquivo, "rb") as f:
        files = {"file": f}
        resp = requests.post(url_upload, files=files, headers=headers)

    if resp.status_code != 200:
        print("❌ Erro no upload:", resp.status_code, resp.text)
        return

    data = resp.json()
    if data.get("status") != "ok":
        print("❌ Erro na resposta da API:", data)
        return

    download_page = data["data"]["downloadPage"]
    print("✅ Upload concluído!")
    print("📄 Página de download:", download_page)

    # --- DOWNLOAD VIA SELENIUM ---
    # Configurações para download automático
    pasta_download = os.path.dirname(caminho_arquivo)
    chrome_options = Options()
    prefs = {"download.default_directory": pasta_download,
             "download.prompt_for_download": False,
             "directory_upgrade": True}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")  # roda em background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Inicializa navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(download_page)
    time.sleep(5)  # espera carregar a página JS

    try:
        # Botão de download
        botao = driver.find_element(By.XPATH, "//a[contains(@class,'downloadButton') or contains(text(),'Download')]")
        botao.click()
        print("🔗 Botão de download clicado!")
        time.sleep(5)  # espera download completar
    except Exception as e:
        print("❌ Erro ao clicar no botão de download:", e)
    finally:
        driver.quit()

    # Renomear arquivo baixado para upload_teste.xlsx
    arquivos = [f for f in os.listdir(pasta_download) if f.endswith(".xlsx")]
    if arquivos:
        ultimo = max([os.path.join(pasta_download, f) for f in arquivos], key=os.path.getctime)
        destino = os.path.join(pasta_download, "upload_teste.xlsx")
        os.rename(ultimo, destino)
        print(f"✅ Arquivo salvo como: {destino}")
    else:
        print("❌ Nenhum arquivo .xlsx encontrado após download.")


if __name__ == "__main__":
    caminho = r"C:/Users/paulo/Downloads/upload_teste.xlsx" #Caminho do arquivo a ser enviado
    token = "UA1ZLz5znWVcZJGPcT8LKV3eJlfT5jhu" #Token da conta Gofile
    upload_e_baixar_gofile(token, caminho)






