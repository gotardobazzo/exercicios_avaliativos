from exercicios_avaliativos._02.contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, taxamensal):
        super().__init__()
        self.__taxamensal = taxamensal

    def get_taxamensal(self):
        return self.__taxamensal()

    def set_taxamensal(self, __taxamensal):
        return self.set_taxamensal(__taxamensal)

    def cadastro_ccorrente(self):
        print ('Obrigado por escolher nossos serviços! \n Siga os passos a seguir para a criação'
               'da conta')
        cpf = input('Informe seu cpf: ')
        senha = int(input('Digite sua senha: '))
        print('A taxa mensal atual é de R$13, que serão descontados de sua conta mensalmente')
        print('O número de sua agência é 0950-5')
        print('O número de sua conta é 51051-4')

        ContaCorrente.set_cpf(cpf)
        ContaCorrente.set_senha(senha)

