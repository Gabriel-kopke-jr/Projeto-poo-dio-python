from conta import Conta
from transacao import Transacao


class Cliente:

    def __init__(self,endereco:str,contas:list):
        self.endereco = endereco
        self.contas = contas

    def adicionar_conta(self,conta):
        try:
            self.contas.append(conta)
            return 'Operação feita com sucesso'
        except Exception as error:
            return f"Operacao não realizada - {error}"

    def realizar_transacao(self,conta:Conta,transacao:Transacao):
        transacao.registrar(conta)
