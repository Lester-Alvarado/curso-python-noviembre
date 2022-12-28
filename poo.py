class Casa():
  color = "amarillo"
  numeracion = None
  frente = "10 mts"
  fondo = "20 mts"
  dueño = None
  registrada = None

  def __init__(self, is_registrada):
    self.registrada = is_registrada

  def pintar(self, nuevo_color):
    self.color = nuevo_color

  def vender(self, nuevo_dueño):
    self.dueño = nuevo_dueño
    print("Casa vendida exitosamente")

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