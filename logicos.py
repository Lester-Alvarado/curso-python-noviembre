# Conjuncion and
print(12 > 2 and 50 < 10)

# Disyuncion or
print(9 != 6 or 8 <= 5)

# Negacion not
print(not True)

edad = 18
nacionalidad = "guatemalteco"

if edad >= 18 and nacionalidad == "guatemalteco":
  print("Puede Votar")
else:
  print("No puede ")

def validar_persona_para_votar(edad,nacionalidad):
  if edad >= 18:
    if nacionalidad == "guatemalteco":
      print("Puede votar")
    else:
      print("No puede votar por nacionalidad")
  else:
    print("No puede votar por la edad")

validar_persona_para_votar(18, "colombiano")

def validar_persona_refactor(edad, nacionalidad):
  if edad < 18:
    print("No puede votar por la edad")
    return

  if nacionalidad != "guatemalteco":
    print("No puede votar por la nacionalidad")
    return

  print("Puede votar")

validar_persona_refactor( 18, "salvadoreño")
