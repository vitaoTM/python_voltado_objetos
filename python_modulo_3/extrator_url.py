class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL esta vazia")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao +1:]
        return url_parametros

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]