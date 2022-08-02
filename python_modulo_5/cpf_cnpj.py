# from validate_docbr import CPF, CNPJ
from validate_docbr import CPF, CNPJ

class Cpf_Cnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == 'cpf':
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF invalido")
        elif self.tipo_documento == 'cnpj':
            if self.valida_cnpj(documento):
                self.cnpj = documento
            else: 
                raise ValueError("CNPJ Invalido!!")
        else:
             raise ValueError("Documento invalido")


    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(cpf)
        else:
            raise ValueError("Quantidade de Digitos invalida")

    def format_Cpf(self):
        mask_cpf = CPF()
        return mask_cpf.mask(self.cpf)

    def format_Cnpj(self):
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_Cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_Cnpj()
        

    def valida_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)
        else: 
            raise ValueError("Quantidade de digitos invalido")