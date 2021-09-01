from genero import Genero
from artista import Artista
from disco import Disco

class Main:
    def __init__(self):
        self.genero = Genero(genero=str)
        self.artista = Artista(nomeartista=str)
        self.disco = Disco()

    def menu(self):
        print('|_____________________________________________________________________|')
        print('|SEJA BEM VINDO À NOSSA LOJA DE DISCOS! POR FAVOR, ESCOLHA UMA OPÇÃO:_|')
        print('|_____________________________________________________________________|')
        print('|1 - Cadastrar artista:_______________________________________________|')
        print('|2 - Excluir artista:_________________________________________________|')
        print('|3 - Cadastrar gênero:________________________________________________|')
        print('|4 - Excluir gênero:__________________________________________________|')
        print('|5 - Cadastrar disco:_________________________________________________|')
        print('|6 - Excluir os discos:_______________________________________________|')
        print('|7 - Listar todos os discos:__________________________________________|')
        print('|8 - Listar todos os discos de um gênero:_____________________________|')
        print('|9 - Listar todos os discos de um artista:____________________________|')
        print('|0 - Sair:____________________________________________________________|')
        print('|_____________________________________________________________________|')

    def opcoesmenu (self):
        pergunta = input("Digite aqui qual escolha deseja: ")
        if pergunta == 0:
            pass

        elif pergunta == 1:
            self.artista = Artista

        elif pergunta == 3:
            self.genero = Genero

        elif pergunta == 5:
            self.disco = Disco


main = Main()
main.menu()
main.opcoesmenu()
