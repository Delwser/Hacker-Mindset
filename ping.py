import requests
alvo = input("Defina o alvo! ex:(https://google.com.br)\n ")
requests.get(alvo, params=None)
print(requests.status_codes)