import re
class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_tel(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto")

    def valida_tel(self, telefone):
        padrao = "[0-9]{2}?[ ]?[0-9]{4,5}[-]?[0-9]{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False