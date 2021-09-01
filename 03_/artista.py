class Artista:
    def __init__(self, nomeartista):
        self.__nomeartista = nomeartista

    def set_artista(self, __nomeartista):
        return self.__nomeartista(__nomeartista)

    def artistanome(self):
        artista = input('Digite aqui o nome do artista que você deseja cadastrar ao catálogo: ')
        self.artistanome = artista
