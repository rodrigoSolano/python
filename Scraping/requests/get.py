import requests

#Realiza una peticion 'get' a la pagina
resp = requests.get('https://dle.rae.es/a?m=31')

print(resp)