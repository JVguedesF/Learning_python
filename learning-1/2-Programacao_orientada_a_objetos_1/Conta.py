class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        # Inicializa os atributos da conta
        self.__numero = numero  # Número da conta
        self.__titular = titular  # Titular da conta
        self.__saldo = saldo  # Saldo da conta
        self.__limite = limite  # Limite de saque

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        # Adiciona um valor ao saldo da conta
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        # Método privado para verificar se é possível sacar um valor
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        # Realiza um saque na conta, desde que seja possível
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        # Transfere um valor para outra conta (destino)
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        # Propriedade para acessar o saldo da conta
        return self.__saldo

    @property
    def get_titular(self):
        # Propriedade para acessar o titular da conta
        return self.__titular

    @property
    def limite(self):
        # Propriedade para acessar o limite de saque da conta
        return self.__limite

    @limite.setter
    def limite(self, limite):
        # Setter para definir o limite de saque da conta
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        # Método estático que retorna o código do banco
        return "001"

    @staticmethod
    def codigos_bancos():
        # Método estático que retorna um dicionário de códigos de bancos
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}