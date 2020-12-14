"""
para poder devolver paginas html y no solo texto, es necesario primero tener una
carpeta con en nombre templates, si no existe una carpeta con este nombre no
funcionara.En esta carpeta es en donde de almacenaran las páginas html,css y js.
Para devolver html, se importa el modulo render_template, con el metodo
render_template(<name.html>)
"""
#Con set FLASK_APP=<namemodule> y flask run se inicia la aplicacion
#Importar el modulo flask
from flask import Flask,render_template
#Crear una instancia de la clase
app = Flask(__name__)

#Definicion de una funcion
#Definicion de una ruta
#Mas de una ruta para una funcion
@app.route("/home")
@app.route("/")
def index():
    #num = 0
    num = [0,1,2,3,4,5,6,7,8,9,10]
    return render_template("index.html",num=num) 

@app.route("/contacto")
def contacto():
    return  "<h1>contacto</h1>"
#Ruta con parametros
@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"Hola {nombre}"

#Inicia servidor con seguimiento de los cambios que se realizen
#No es recomenbable en produccion
if __name__ == "__main__":
    app.run(debug=True)