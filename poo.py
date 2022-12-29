class Casa():
  color = "amarillo"
  numeracion = None
  frente = "10 mts"
  fondo = "20 mts"
  dueño = None
  registrada = None

  def __init__(self, is_registrada):
    self.registrada = is_registrada

  def __str__(self) -> str:
    return f"""
Esta es una casa
El dueño es {self.dueño}
El color es {self.color}
"""

  def __repr__(self) -> str:
    return f"Casa numero {self.numeracion}"

  def pintar(self, nuevo_color):
    self.color = nuevo_color

  def vender(self, nuevo_dueño):
    self.dueño = nuevo_dueño
    print("Casa vendida exitosamente")

  def __entregar_llaves(self):
    print("Se entrega las llaves de la Casa")

  def gestionar_llaves(self, receptor):
    if receptor != self.dueño:
      raise Exception("No se pueden entregar llaves a alguien que no sea el dueño")
    
    self.__entregar_llaves()

  @staticmethod
  def get_atributos_obligatorios():
    return ("is_registrada")

casa1 = Casa(is_registrada=True)
print(type(casa1))
print(casa1.color)
print(casa1.numeracion)
casa1.numeracion = "A1"
print(casa1.numeracion)
casa1.pintar("Azul")
print(casa1.color)
casa1.vender("Lester Alvarado")

casa2 = Casa(is_registrada=False)
print(casa1.color)
print(casa2.color)
print(casa1)
print(casa2)

casa1.gestionar_llaves("Lester Alvarado")


print(Casa.get_atributos_obligatorios())
print(repr(casa1))