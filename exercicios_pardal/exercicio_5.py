import requests

def buscando_urls():
    with open("lista_1.txt", "r") as arquivo: #Abrindo o arquivo, e lendo ele.
        urls = arquivo.readlines() #Definindo quais tipos de 
        #import ipdb;ipdb.set_trace()
        for linha in range(0, len(urls)):  # Puxando as primeiras 20 linhas
            url = "https://fiap.com.br/" + urls[linha].strip()  # Adicionando https para fazer requisição
            response = requests.get(url)  # Fazendo a requisição
            if response.status_code == 200:
                print(f"O site {url} retornou status: {response.status_code}") #Retornando apenas aqueles que derem valor de 200
            elif response.status_code in (301, 302): #Fazendo requisição de arquivos dentro de um diretório.
                print(f"Diretório encontrado em {url}, iniciando a procura de arquivos...")
                lista_arquivos = ["main.css", "index.html", "about.html", "contact.html", "styles.css", "app.js", "logo.png", "main.js", "index.php", "login.php", "dashboard.php"]
                for arquivo in lista_arquivos:
                    dir_url = url + arquivo
                    respo = requests.get(dir_url)
                    if respo.status_code == 200:
                        print(f"Arquivo Encontrado: {dir_url}")
                    else:
                        pass
            else:
                pass
            


buscando_urls()