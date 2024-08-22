import requests

def buscando_urls():
    with open("subdomains-top1million-5000.txt", "r") as arquivo: #Abrindo o arquivo, e lendo ele.
        urls = arquivo.readlines() #Definindo quais tipos de 
        
        for i in range(0, 20):  # Puxando as primeiras 20 linhas
            url = "https://" + urls[i].strip() +".example.com/"  # Adicionando https para fazer requisição
            
            try:
                response = requests.get(url)  # Fazendo a requisição
                print(f"O site {url} retornou status: {response.status_code}")
            except requests.exceptions.ConnectionError:
                print(f"A requisição falhou para o site {url}")

buscando_urls()
