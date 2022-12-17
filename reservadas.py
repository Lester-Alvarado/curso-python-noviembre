def saludar():
  print("Saludos a Todos")

nombre = "Lester"
print(nombre)

# Esta variable es un string
apellido = "Alvarado"

# Entero
edad = 15
print(type(edad))

# Decimales
peso = 1.50
print(type(peso))

print(edad + peso)

peso = 2


is_adult = True
habilitar_noticias = False

print(nombre + " " + apellido)
print(f"{nombre} {apellido}")

# Evitar sumar distintos tipos de datos
#nombre + edad
print(nombre + str(edad))

# Listas o arreglos o arrays
alumnos = ["Angel", "Byron", "Deeivin", "Diego", 15, True, edad]
print(alumnos)
print(alumnos[1])

# # Diccionarios
persona = {
  "nombre": "Rafael",
  "apellido": "Flores",
  "genero": "Masculino",
  "edad": 54,
  "es_adulto": True,
  "altura": 1.72
}

print(persona["edad"])

estudiantes = [
  {"nombre": "Ruben", "apellido": "Hernandez"},
  {"nombre": "Oscar", "apellido": "Hernandez"},
  {"nombre": "Lester", "apellido": "Alvarado"}
]
print(estudiantes[2]["nombre"])
