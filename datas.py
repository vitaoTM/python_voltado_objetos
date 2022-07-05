class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print(f'{self.dia:11}/{self.mes:02}/{self.ano}')

data = Data(11,2,1992)
   
data.formatada()
