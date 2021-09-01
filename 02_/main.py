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
            print('1 - Depósito')
            print('2 - Saque')
            opcaopp = input('Digite a opção entre as desejadas: ')
            if opcaopp == '1':
                self.contabancaria.deposito()
            elif opcaopp == '2':
                self.contabancaria.saque()

        elif opcao == '2':
            self.contacorrente.cadastro_ccorrente()
            print('1 - Aumento de Limite da Conta Corrente')
            print('2 - Depósito')
            print('3 - Saque')
            opcaocc = input('Digite a opção entre as desejadas: ')
            if opcaocc == '1':
                self.contacorrente.aumentolimite()
            elif opcaocc == '2':
                self.contabancaria.deposito()
            elif opcaocc == '3':
                self.contabancaria.saque()

        elif opcao == '3':
            pass

main = Main()
main.menu()
main.opcoesmenu()
