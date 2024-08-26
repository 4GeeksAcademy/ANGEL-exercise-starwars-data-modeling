
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    eye_color = Column(String(255), nullable=False) 
    gender = Column(String(255), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    clima = Column(String(255), nullable = False)
    diametro = Column(String(255), nullable = False)

class Vehiculo(Base): 
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(255), nullable=False)
    pasajeros = Column(String(255), nullable=False)
    costo = Column(String(255), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable = True)
    usuario = relationship(Usuario)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable = True)
    personaje = relationship(Personaje)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable = True)
    planeta = relationship(Planeta)
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'), nullable = True)
    vehiculo = relationship(Vehiculo)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
