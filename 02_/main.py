from contabancaria import ContaBancaria
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

#aumento_limite = ContaCorrente.aumentolimite()


class Main:
    def __init__(self):
       self.contabancaria = ContaBancaria()
       self.contacorrente = ContaCorrente()
       self.contapoupanca = ContaPoupanca()
    def menu(self):

        print('---------')
        print('--BANCO--')
        print('---------')
        print('1 - Cadastro de Conta Poupança')
        print('2 - Cadastro de Conta Corrente')
        print('3 - Aumento de Limite da Conta Corrente')
        print('4 - Depósito')
        print('5 - Saque')
        print('6 - Sair')
        print('---------')

    def opcoesmenu(self):
        opcao = input('Digite sua escolha: ')
        if opcao == '1':
            self.contacorrente.cadastro_ccorrente()
            print('Você é obrigado a fazer um depósito inicial')
            self.deposito()
        elif opcao == '2':
            self.contapoupanca.cadastro_cpoupanca()
        elif opcao == '3':
            self.contacorrente.aumentolimite()
        elif opcao == '4':

        elif opcao == '5':
            ''
        elif opcao == '6':
            print('Obrigado por usar os serviços')
            pass

    def deposito(self):
        valor = 0
        valor = input('Digite o valor que você deseja depositar:')

