'''
Para cualquier petición, es posible especificar un timeout de espera de respuesta.
Para ello, debes indicar en el parámetro timeout los segundos que la petición debe esperar, como mucho,
antes de recibir el primer byte.
Si no se especifica un timeout, el request esperará indefinidamente por una respuesta.
Si el servidor no devuelve una respuesta en el timeout especificado, se lanzara una excepción del tipo:
requests.exceptions.Timeout

En caso de que se produzca algún error al realizar la petición, se lanzara una excepción.
La base de todas las excepciónes de un requests es requests.exceptions.RequestException.
Otras excepciones bastante comunes son las siguientes:
Timeout: Si el servidor no devuelve una respuesta en en tiempo indicado en el parametro timeout
TooManyRedirects: Si una peticion excede en número de redireccionamientos máximo.
ConnectionError: Si existe algún problema en la red.

Por defecto, al realizar una petición con requests, esta sigue las redirecciones que vaya indicando el 
servidor antes de devolver la respuesta definitiva (excepto para HEAD, que hay que indicarlo explícitamente).
Si esto ocurre, el objeto con la respuesta guarda en el atributo history una lista con todas las respuestas
desde la más antigua a la más reciente.
Para modificar este comportamiento, debes establecer el parámetro allow_redirects con valor False.

'''
import requests

def peticionSeguimiento():
    try:

        r = requests.get('https://google.com')
        print(r.history)
        print(r.status_code)
        print(r.url)
    except requests.exceptions.Timeout:
        print("Error")
    

if __name__ == "__main__":
    peticionSeguimiento()
    
try:
    resp = requests.get('https://dle.rae.es/a?m=form',timeout=0.01)
except requests.exceptions.Timeout:
    print("Tiempo de espera excedido")