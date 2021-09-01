
from disco import Disco
from artista import Artista
from genero import Genero

class Dicionarios:
    def __init__(self, dicionarios):
        self.__genero = Genero
        self.__artista = Artista
        self.__disco = Disco
        self.__dicionarios = dicionarios



main = Dicionarios(dicionarios=str)
main.dicionarios(dicionarios=str)


