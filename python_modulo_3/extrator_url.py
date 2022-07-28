class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL esta vazia")