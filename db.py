# SELECT * FROM users where id = 1
# INSERT INTO users (id, name, ege) (1, "Lester", 15)
# ORM - Object Relational Mapper
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, delete
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
engine = create_engine("sqlite:///:memory:")

class Alumno(Base):
  __tablename__ = "alumnos"

  # id, nombres, apellidos, carnet
  id = Column(Integer, primary_key=True)
  nombres = Column(String, nullable=False)
  apellidos = Column(String, nullable=False)
  carnet = Column(Integer)

  @hybrid_property
  def nombre_completo(self):
    return f"{self.nombres} {self.apellidos}"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


alumno = Alumno(
  nombres="Diana",
  apellidos="Perez",
  carnet=1234
)
print(alumno.nombres)
print(alumno.id)
session.add(alumno)


alumno2 = Alumno(
  nombres="Milton",
  apellidos="Juarez",
  carnet=5678
)
session.add(alumno2)
session.commit()
print(alumno2.nombre_completo)

session.refresh(alumno2)
print(alumno2.id)

alumno_db = session.query(Alumno).where(Alumno.nombres == "Diana").first()
print(alumno_db.apellidos)
print(alumno_db.id)

alumnos = session.query(Alumno).all()
print(alumnos)
print(alumnos[1].id)
print(alumnos[1].nombres)

cantidad_alumnos = session.query(Alumno).count()
print(f"La cantidad de Alumnos es: {cantidad_alumnos}")

alumno_db.nombres = "Dianah"
session.add(alumno_db)
session.commit()

borrado = delete(Alumno).where(Alumno.id == 1)
session.execute(borrado)

alumno_borrado = session.query(Alumno).where(Alumno.id == 1).first()
print(alumno_borrado)