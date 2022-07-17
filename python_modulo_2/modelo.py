from pyparsing import anyOpenTag


class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme('vingadores - Guerra infinita' , 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

westworld = Series('westworld', 2016, 4)
print(f'Nome {westworld.nome} - Ano {westworld.ano} -'
        f' Temporada {westworld.temporadas} -' 
        f'Likes: {westworld.likes}')

