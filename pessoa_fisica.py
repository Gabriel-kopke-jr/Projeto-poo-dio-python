from cliente import Cliente


class PessoaFisica(Cliente):

        def __init__(self,cpf,nome,data_nascimento,endereco,contas):
            self.cpf = cpf
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.endereco = endereco
            self.contas = contas