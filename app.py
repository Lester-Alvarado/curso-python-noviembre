from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_word():
  return "Hola Mundo"

@app.route('/edad/<int:edad_persona>')
def verificar_edad(edad_persona):
  if edad_persona >= 18:
    return "Es un adulto"
  else:
    return "No es un adulto"

@app.route("/saludo", methods=["POST"])
def saludar():
  return "Saludos a todos desde el POST"

@app.route("/saludo", methods=["PUT"])
def saludar_get():
  return "Saludos a todos desde el PUT"


@app.route("/users", methods=["POST"])
def registrar():
  return {
    "metodo": request.method,
    "nombre": request.form["nombre"],
    "edad": request.form["edad"]
  }

@app.route("/query")
def return_query_params():
  return request.args.get("key", "valor-defecto")

@app.errorhandler(404)
def not_found(error):
  return "Ups este endpoint no existe"