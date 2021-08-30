from contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, taxamensal, aumento, saldocc, depositocc, saquecc):
        super().__init__()
        self.__taxamensal = taxamensal
        self.__aumento = aumento
        self.__saldocc = saldocc
        self.__depositocc = depositocc
        self.__saquecc = saquecc

    def set_aumento(self, __aumento):
        return self.set_aumento(__aumento)

    def set_depositocc(self, __deposito):
        return self.set_deposito(__deposito)

    def set_saquecc(self, __saquecc):
        return self.set_saquecc(__saquecc)

    def get_saldocc(self, __saldocc):
        return self.__saldocc

    def set_saldocc(self, __saldocc):
        return self.__saldocc

    @staticmethod
    def cadastro_ccorrente():

        print('Obrigado por escolher nossos serviços! \n Siga os passos a seguir para a criação'
               'da conta')
        cpf = input('Informe seu cpf: ')
        senha = int(input('Digite sua senha: '))
        print('A taxa mensal atual é de R$13, que serão descontados de sua conta mensalmente')
        print('O número de sua agência é 0950-5')
        print('O número de sua conta é 51051-4')

        ContaCorrente.set_cpf(cpf)
        ContaCorrente.set_senha(senha)

    @staticmethod
    def aumentolimite():
        global aument0
        aument0 = input('Você deseja aumentar o limite da sua conta corrente? S/N ')
        if aument0 == 'S' or 's':
            aument0 = int(input('Digite o valor do aumento. O máximo do limite é R$50: '))
            if aument0 >= 50:
                print('Valor não disponível')
            else:
                print('O valor do limite da conta foi corrigido')
        elif aument0 == 'N' or 'n':
            pass
        else:
            print('Valor inválido')

        ContaCorrente.set_aumento(aument0)
