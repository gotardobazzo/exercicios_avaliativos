class Genero:
    def __init__(self, genero):
        self.__genero = genero

    def set_genero(self, __genero):
        return self.__genero(__genero)

    def generonome(self):
        genero = input('Digite aqui o nome do gênero que você deseja adicionar: ')
        self.__genero = genero
