import re

from numpy import extract, quantile
class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url)
        e verifica se a url é valida.
        """
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        """Retona a url removendo os espaços em branco.
        """
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("A URL esta vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é valida")
        
    
    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        """Retorna os parametros dda url."""
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao +1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    

url= "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino =="dolar":
    valor_convercao = int(quantidade) / valor_dolar
    print(f"O valor de R$ {quantidade} reais é igual a $ {valor_convercao} dolares")
elif moeda_origem == "dolar" and moeda_destino =="real":
    valor_convercao = int(quantidade) * valor_dolar
    print(f'O valor de $ {quantidade} dolares é igual a {valor_convercao} reais')
else:
    (f'Cambio de {moeda_origem} para {moeda_destino} não está disponivel')

