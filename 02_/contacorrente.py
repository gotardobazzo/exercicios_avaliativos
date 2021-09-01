from contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        super().__init__()

    def set_aumento(self, __aumento):
        return self.set_aumento(__aumento)

    def limitesaque(self, saldo, limitesaque):
        self.__limitesaque = limitesaque
        global limite
        limite = 50
        limitesaque = int(saldo) + limite

    def cadastro_ccorrente(self):

        print('Obrigado por escolher nossos serviços! \n Siga os passos a seguir para a criação'
               'da conta')
        cpf = input('Informe seu cpf: ')
        senha = int(input('Digite sua senha: '))
        print('A taxa mensal atual é de R$13, que serão descontados de sua conta mensalmente')
        print('O número de sua agência é 0950-5')
        print('O número de sua conta é 51051-4')

        self.__cpf = cpf
        self.__senha = senha

    def aumentolimite(self):
        global aument0
        aument0 = input('Você deseja aumentar o limite da sua conta corrente? S/N ')
        if aument0 == 'S' or 's':
            aument0 = int(input('Digite o valor do aumento. O máximo do limite é R$100: '))
            if aument0 >= 50:
                print('Valor não disponível')
            else:
                print('O valor do limite da conta foi corrigido')
        elif aument0 == 'N' or 'n':
            pass
        else:
            print('Valor inválido')
        aument0 = limite

        ContaCorrente.set_aumento(aument0)
