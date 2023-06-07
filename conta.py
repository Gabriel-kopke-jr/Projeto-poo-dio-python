import uuid

from cliente import Cliente
from historico import Historico


class Conta:

    def __init__(self):
        self.agencia = '01',


    def saldo(self):
        print(f'O seu saldo atual é de {self.saldo_conta}')

    def nova_conta(self,cliente: Cliente):
        self.numero_conta = str(uuid.uuid4())
        self.cliente = cliente
        self.saldo_conta = 0
        self.historico = Historico

    def sacar(self,valor)->bool:
        if valor < self.saldo_conta:
            self.saldo_conta -= valor
            return True
        else:
            print(f"Operação não concluida: Você não pode realizar este saque devido a insuficiencia de saldo. Seu saldo atual é  {self.saldo_conta}")


    def depositar(self,valor)-> bool:
        if valor >= 0:
            self.saldo_conta += valor
        return True
