from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola, Estudiantes del tec!</p>"

@app.route("/Nombre")
def hello(nombre):
    return f"<h2>Hola, Estimado: {nombre}</h2>"

@app.route("/about")
def about():
        return"<h1>Esta es la pagina about</h1>"

app.route("/about")
def about():
    return "<h1>Esta es la pagina de about</h1>"
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000, debug=True)
