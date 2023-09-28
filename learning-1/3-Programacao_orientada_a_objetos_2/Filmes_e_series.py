class Programa:
    def __init__(self, nome, ano):
        # Inicializa um programa com um nome, ano e número inicial de likes.
        self._nome = nome.title()  # O nome do programa (com a primeira letra em maiúscula)
        self.ano = ano  # O ano de lançamento do programa
        self._likes = 0  # O número de likes (inicializado com 0)

    @property
    def likes(self):
        # Propriedade para acessar o número de likes.
        return self._likes

    def dar_likes(self):
        # Método para dar um like ao programa.
        self._likes += 1

    @property
    def nome(self):
        # Propriedade para acessar o nome do programa.
        return self._nome

    @nome.setter
    def nome(self, nome):
        # Setter para definir o nome do programa.
        self._nome = nome

    def __str__(self):
        # Retorna uma representação em string do programa.
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # Inicializa um filme com nome, ano, e duração.
        super().__init__(nome, ano)
        self.duracao = duracao  # Duração do filme em minutos.
    
    def __str__(self):
        # Retorna uma representação em string do filme.
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # Inicializa uma série com nome, ano e número de temporadas.
        super().__init__(nome, ano)
        self.temporadas = temporadas  # Número de temporadas da série.

    def __str__(self):
        # Retorna uma representação em string da série.
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist():
    def __init__(self, nome, programas):
        # Inicializa uma playlist com um nome e uma lista de programas.
        self.nome = nome  # Nome da playlist.
        self._programas = programas  # Lista de programas.

    def __getitem__(self, item):
        # Permite acessar programas da playlist como se fosse uma lista.
        return self._programas[item]

    def __len__(self):
        # Retorna o número de programas na playlist.
        return len(self._programas)

# Criando instâncias de filmes e séries.
vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

# Dando likes aos programas.
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

# Criando uma lista de programas.
listinha = [atlanta, vingadores, demolidor, tmep]

# Criando uma playlist.
minha_playlist = Playlist('Fim de Semana', listinha)

# Iterando sobre os programas na playlist e imprimindo suas informações.
for programa in minha_playlist:
    print(programa)

# Imprimindo o tamanho da playlist.
print(f'Tamanho: {len(minha_playlist)}')