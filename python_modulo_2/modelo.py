from re import I
from numpy import atleast_1d
from pyparsing import anyOpenTag

class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__likes = 0
        self.ano = ano
    
    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'
        
    @property
    def likes(self):
        return self.__likes
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'  

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    @property
    def listagen(self):
        return self._programas
    @property
    def tamanho(self):
        return len(self._programas)


demolidor = Series('demolidor', 2016, 4)
vingadores = Filme('vingadores - Guerra infinita' , 2018, 160)
westworld = Series('westworld', 2016, 4)

westworld.dar_like()
demolidor.dar_like()
vingadores.dar_like()
vingadores.dar_like()
westworld.dar_like()


playlist = [vingadores, westworld, demolidor]

fim_de_semana = Playlist('fim de semana', playlist)

print(f'Tamanho da playlist: {len(playlist)}')

for programa in playlist:
    print(programa)

print(f'Ta ou nao ta ? {demolidor in playlist}')

# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

# print(f'Nome {westworld.nome} - Ano {westworld.ano} -'
#         f' Temporada {westworld.temporadas} -' 
#         f'Likes: {westworld.likes}')
