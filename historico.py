from transacao import Transacao


class Historico():

    historico = []

    def adicionar_transacao(self, transacao:Transacao):
        self.historico.append(transacao)

