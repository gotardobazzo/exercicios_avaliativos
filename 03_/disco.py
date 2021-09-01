from genero import Genero
from artista import Artista

class Disco(Genero, Artista):
    def __init__(self):
        super(Disco, self).__init__(Genero)
        super(Disco, self).__init__(Artista)

    def set_disco(self, __nomeartista, __genero, __disco):
        return self.__disco(__disco)

    def disco (self):
        disco = input('Digite aqui o nome do disco que você deseja adicionar: ')
