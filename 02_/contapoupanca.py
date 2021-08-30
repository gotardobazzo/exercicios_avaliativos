from contabancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, taxajuro):
        super().__init__()
        self.__taxajuro = taxajuro
        self.__depositopp = depositopp
        self.__saquepp = saquepp

    def get_taxajuro(self):
        return self.__taxajuro()

    def set_taxajuro(self, __taxajuro):
        return self.set_taxajuro(__taxajuro)

    def set_depositopp(self, __depositopp):
        return self.set_depositopp(__depositopp)

    def set_saquepp(self, __saquepp):
        return self.set_saquepp(__saquepp)

    @staticmethod
    def cadastro_cpoupanca():
        print('Obrigado por escolher nossos serviços! \n Siga os passos a seguir para a criação'
               'da conta')
        cpf = input('Informe seu cpf: ')
        senha = int(input('Digite sua senha: '))
        print('A taxa de juros atual é de 2%, que será somado ao seu saldo mensalmente')
        print('O número de sua agência é 0950-5')
        print('O número de sua conta é 51051-4')

        ContaPoupanca.set_cpf(cpf)
        ContaPoupanca.set_senha(senha)

    @staticmethod
    def depositopoupanca():
        global deposito
        deposito = input('Digite o valor que você deseja depositar: ')
        if deposito > '2000':
            print('Este valor é alto demais')
        else:
            ContaPoupanca.set_deposito(deposito)

    @staticmethod
    def saquepoupanca():
        saque = input('Digite o valor que você deseja sacar: ')
        if saque > deposito:

        ContaPoupanca.set_saque(saque)
