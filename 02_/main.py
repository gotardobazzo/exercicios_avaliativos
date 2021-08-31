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
        print('3 - Sair')
        print('---------')

    def opcoesmenu(self):
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            self.contapoupanca.cadastro_cpoupanca()

        #print('3 - Aumento de Limite da Conta Corrente')
        #print('4 - Depósito')
        #print('5 - Saque')

        elif opcao == '2':
            self.contacorrente.cadastro_ccorrente()

        elif opcao == '3':
            pass

main = Main()
