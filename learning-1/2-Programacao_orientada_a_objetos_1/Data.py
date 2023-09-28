class Data:

    def __init__(self, dia, mes, ano):
        # Inicializa os atributos da data
        self.dia = dia  # Dia
        self.mes = mes  # Mês
        self.ano = ano  # Ano

    def formatada(self):
        # Método para imprimir a data formatada
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))