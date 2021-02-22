# #SEM ABSTRAÇÃO E ENCAPSULAMENTO
# class Conta:
#     contador = 400

#     def __init__(self, titular, saldo, limite):
#         self.numero = Conta.contador
#         self.titular = titular
#         self.saldo = saldo
#         self.limite = limite
#         Conta.contador += 1

#     def extrato(self):
#         print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

#     def depositar(self, valor):
#         self.saldo += valor

#     def sacar(self, valor):
#         self.saldo -= valor

# conta1 = Conta('Luciana', 10.00, 1000.00)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)

# #sem encapsulamento, posso alterar meu saldo livremente
# conta1.saldo = 9999999999999999999
# print(f'O novo saldo de {conta1.titular} é de {conta1.saldo}')

"""
ENTÃO O JEITO CERTO É O SEGUITE:
"""
class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        #preciso validar que um depósito sempre será positivo
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        #preciso validar que um saque precisa ser maior que zero e de até o valor que tenho em conta
        if valor > 0:
            if self.saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo')

conta1 = Conta('Luciana', 10.00, 1000.00)
print(conta1.__dict__)

