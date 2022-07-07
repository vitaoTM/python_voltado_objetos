from pyparsing import anyOpenTag


class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filmes('vingadores - Guerra infinita' , 2018, 160)
print(vingadores.nome)

westworld = Series('westworld', 2016, 4)
print(f'Nome {westworld.nome} - Ano {westworld.ano} -'
        f' Temporada {westworld.temporadas}')