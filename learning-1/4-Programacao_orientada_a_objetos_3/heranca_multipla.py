class Funcionario:
    def __init__(self, nome):
        # Inicializa um objeto Funcionario com um nome.
        self.nome = nome

    def registra_horas(self, horas):
        # Registra horas de trabalho (método não implementado aqui).
        print('Horas registradas.')

    def mostrar_tarefas(self):
        # Mostra as tarefas do funcionário (método não implementado aqui).
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        # Mostra as tarefas específicas de um funcionário da Caelum.
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        # Mostra os cursos do mês ou do mês especificado.
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    # Não redefine o método mostrar_tarefas, portanto, herda a implementação de Funcionario.
    
    def busca_perguntas_sem_resposta(self):
        # Mostra perguntas não respondidas do fórum da Alura.
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        # Define uma representação em string personalizada para a classe Hipster.
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

# Criando instâncias de funcionários
jose = Junior('José')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()  # Usará a implementação de Alura para mostrar_tarefas

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()  # Usará a implementação de Caelum para busca_cursos_do_mes

luan.mostrar_tarefas()  # Usará a implementação de Caelum para mostrar_tarefas

print(luan)  # Chamará __str__ de Hipster para imprimir a instância
