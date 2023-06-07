import uuid
from conta import Conta
from transacao import Transacao



class Saque(Transacao):
    registros = []

    def registrar(self, conta: Conta):
        id = str(uuid.uuid4())
        self.registros.append(id)

    def sacar(self, valor: float,conta:Conta):
        if valor < 0:
            print("OPERACAO NAO PERMITIDA")
            return
        conta.saldo_conta -= valor
        self.registrar(conta)

