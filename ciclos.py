# while
i = 0
while i <= 10:
  print(i)
  i += 1
print("Ciclo roto")


# For
alumnos = ["Adan", "Jorge", "Andrea", "Gabi", "Andrea"]
for alumno in alumnos:
  print(alumno)


for alumno in alumnos:
  if alumno == "Andrea":
    print("Encontramos a Andrea")
    continue          # "break" para para lectura y "continue" para continuar

  print(alumno)

  nombrePersona = "Lester" # No es la forma de trabajar
  nombre_persona = "Lester" # Esta si es la correcta forma