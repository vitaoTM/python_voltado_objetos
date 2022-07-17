from pyparsing import anyOpenTag




class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__likes = 0
        self.ano = ano
        
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

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - Guerra infinita' , 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

westworld = Series('westworld', 2016, 4)
print(f'Nome {westworld.nome} - Ano {westworld.ano} -'
        f' Temporada {westworld.temporadas} -' 
        f'Likes: {westworld.likes}')

