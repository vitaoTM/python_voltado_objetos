from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        mes_ano = [
            'Janeiro', 'Fevereiro', 'Marco',
            'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return mes_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana = [
            'Domingo', 
            'Segunda',
            'Terça',
            'Quarta',
            'Quinta',
            'Sexta',
            'Sabado'
        ]
        dia_cadastro = self.momento_cadastro.weekday()+1
        return dia_semana[dia_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() )- self.momento_cadastro
        return tempo_cadastro