from exercicios_avaliativos._02.contabancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, taxajuro):
        super().__init__()
        self.__taxajuro = taxajuro

    def get_taxajuro(self):
        return self.__taxajuro()

    def set_taxajuro(self, __taxajuro):
        return self.set_taxajuro(__taxajuro)

    def cadastro_cpoupanca(self):
        print ('Obrigado por escolher nossos serviços! \n Siga os passos a seguir para a criação'
               'da conta')
        cpf = input('Informe seu cpf: ')
        senha = int(input('Digite sua senha: '))
        print('A taxa de juros atual é de 2%, que será somado ao seu saldo mensalmente')
        print('O número de sua agência é 0950-5')
        print('O número de sua conta é 51051-4')

        ContaPoupanca.set_cpf(cpf)
        ContaPoupanca.set_senha(senha)