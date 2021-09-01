class ContaBancaria:
    def __init__(self):
        self.__cpf = ' '
        self.__agencia = ' '
        self.__nconta = ' '
        self.__senha = ' '
        self.__saldo = ' '
        self.__deposito = ' '
        self.__saque = ' '

    def set_cpf(self, __cpf):
        return self.__cpf

    def get_agencia(self):
        return self.__agencia

    def get_nconta(self):
        return self.__nconta

    def set_senha(self, __senha):
        return self.__senha

    def saldo (self):
        saldo = '0'
        ContaBancaria.set_saldo(saldo)

    def set_saldo(self, __saldo):
        return self.__saldo

    def deposito(self, __saldo):
        deposito = input('Digite o valor que você deseja depositar: ')
        if deposito > '2000':
            print('Este valor é alto demais')
        else:
            ContaBancaria.set_deposito(deposito)
        self.saldo = self.saldo + deposito

    def saque(self, __saldo):
        saque = input('Digite o valor que você deseja sacar: ')
        ContaBancaria.set_saque(saque)
        self.saldo = self.saldo - saque

    def get_deposito(self):
        return self.__deposito

    def set_deposito(self, __deposito):
        return self.__deposito

    def get_saque(self):
        return self.__saque

    def set_saque(self, __saque):
        return self.__saque
