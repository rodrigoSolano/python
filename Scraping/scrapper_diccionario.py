import requests
from bs4 import BeautifulSoup

form_data = {'as_word':'hogar'}
response = requests.get('https://www.mercadolibre.com.mx/',data=form_data,timeout=5)
soup = BeautifulSoup(response.text,'lxml')

resultados = soup.find_all("h2")

print(resultados)
