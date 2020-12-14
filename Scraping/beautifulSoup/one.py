'''
Para crear un web scraper con python utilizando BeautifulSoup primero se necesita descargar la pagina web,
para lograr esto utilizaremos la libreria requests.

Despues se crea la 'sopa'. El constructor recibe un objeto response accediendo a su atributo text.

El último paso es hacer una búsqueda en el árbol y obtener los objetos que contienen la información y datos
que necesitamos. Para ello, tienes varias alternativas como veremos en las siguientes secciones.

Objetos que se pueden encontrar en el arbol de de la sopa.

Tag.
Este objeto corresponde a una etiqueta HTML o XML. Ejemplo: soup.title <- etiqueta title
Dado un objeto de tipo tag, podemos acceder a sus atributos tratando al objeto como si fuera un diccionario.
Ademas, se puede acceder a este diccionario por medio del atributo attrs.
NavigableString.
Un objeto de este tipo representa a la cadena de texto que hay contenida en una etiqueta. Se accede por 
medio de la propiedad string

Busquedas y filtros.
Beautiful Soup pone a nuestra disposición diferentes métodos para buscar elementos en el árbol. 
Sin embargo, dos de los principales son find_all() y find().
Ambos métodos trabajan de forma similar. Básicamente, buscan entre los descendientes de un objeto de tipo 
Tag y recuperan todos aquellos que cumplan una serie de filtros.

Filtro por nombre de etiqueta.
El filtro más básico consiste en pasar el nombre de la etiqueta a buscar como primer argumento de la 
función (parámetro name).


Filtro por atributos.
Además del nombre de la etiqueta, puedes especificar parámetros con nombre. Si estos no coinciden con los
nombres de los parámetros de la función, serán tratados como atributos de la etiqueta entre los que filtrar.



'''
import requests
from bs4 import BeautifulSoup

form_data = {'w':'hogar'}
response = requests.get('https://dle.rae.es/',data=form_data,timeout=5)
soup = BeautifulSoup(response.text,'lxml')

resultados = soup.article

print(resultados)

#enlaces = soup.find_all('a')
#for enlace in enlaces:
#    print(enlace.string)
#
#div = soup.div
#primer_parrafo = soup.p
#texto = primer_parrafo.string
#print(texto)
#print(soup.title)
#print(soup.div)
#print(div.attrs)
