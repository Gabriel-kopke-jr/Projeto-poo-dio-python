import uuid

from conta import Conta
from transacao import Transacao


class Deposito(Transacao):
    registros = []


    def __init__(self,valor):
        self.valor = valor

    def registrar(self,conta:Conta):
        id = str(uuid.uuid4())
        self.registros.append(id)

    def depositar(self,conta:Conta,valor):
        if valor > 0:
            conta.saldo_conta += valor
            self.registrar(conta)
        else:
            print(f"Transação não permitida")


