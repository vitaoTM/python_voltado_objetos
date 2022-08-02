# from validate_docbr import CPF, CNPJ
from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido")

    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            return ValueError("Quantidade de Digitos invalida")

    def format_Cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)        

    def __str__(self):
        return self.format_Cpf()