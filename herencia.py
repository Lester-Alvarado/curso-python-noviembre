class Vehiculo():
  ruedas = None
  
  def avanzar(self):
    print("El vehiculo esta avanzando")

class Carro(Vehiculo):
  ruedas = 4

  def avanzar(self):
    print("Avanzando en un Carro")

class Moto(Vehiculo):
  pass

nissan = Carro()
nissan.avanzar()
print(nissan.ruedas)

yamaha = Moto()
yamaha.avanzar()

Vehiculo = Vehiculo()