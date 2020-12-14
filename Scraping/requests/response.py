'''
El objeto response es el que contiene toda la informacion referente a la respuesta.

Contenido.
Cuando la respuesta que devuelve un servidor es de tipo texto,
por ejemplo html o xml, el contenido se encuentra en el atributo text del objeto Response.

requests automáticamente decodifica el contenido devuelto por el servidor, adivinando la codificación a 
emplear a partir de las cabeceras de la respuesta. Para conocer la codificación empleada puedes acceder al 
atributo encoding.

Para aquellos casos en los que la respuesta no es texto, como por ejemplo una imagen o un pdf, entonces se
debe acceder al atributo content, ya que este devuelve el contenido como una secuencia de bytes.

Para obtener el código de estado de la respuesta, debes acceder al atributo status_code de la misma.

Las cabeceras de la respuesta están accesibles a través del atributo headers. Este atributo es un diccionario 
especial que contiene cada una de las cabeceras devueltas como claves del diccionario.

Si quieres consultar las cookies devueltas por el servidor, lo puedes hacer accediendo al atributo cookies
de la respuesta. Este atributo es de tipo RequestsCookieJar, que actúa como un diccionario con mejoras, 
para indicar el dominio y/o el path de una cookie, entre otras cosas:
'''

import requests

response = requests.get("https://dle.rae.es/",timeout=5)

#print(response.text)
#print(response.encoding)
#print(response.headers)
print(response.cookies)