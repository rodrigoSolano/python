import requests

#Name del campo del formulario y el valor a asignar
auth_data = {'w':'a'}
resp = requests.post('https://dle.rae.es/',auth_data)

'''
Para el caso en que un formulario tenga uno o más campos multivaluados, se pueden especificar los diferentes 
valores de dos maneras distintas.
En un diccionario, indicando una lista de valores para una clave:

form_data = {'color': ['blanco', 'verde'], 'idioma': 'es'}
resp = requests.post('http://mipagina.xyz/formulario/', data=form_data)

O como una lista de tuplas:

form_data = [('color', 'blanco'), ('color', 'verde'), ('idioma', 'es')]
resp = requests.post('http://mipagina.xyz/formulario/', data=form_data)

'''

print(resp)