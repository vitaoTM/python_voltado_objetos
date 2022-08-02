# from validate_docbr import CPF, CNPJ
from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento) 
        else:
            raise ValueError("Quantidade de digitos está incorreta")

class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Invalido")

    def __str__(self):
        return self.format()
        

    def valida(self, documento):
        valida = CPF()
        return valida.validate(documento)
    
    def format(self):
        mask_cpf = CPF()
        return mask_cpf.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento 
        else:
            raise ValueError("CNPJ invalido")

    def __str__(self):
        return self.format()
            

    def valida(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def format(self):
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)         



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


    # def valida_cpf(self, cpf):
    #     if len(cpf) == 11:
    #     else:
    #         raise ValueError("Quantidade de Digitos invalida")

    # def format_Cpf(self):

    # def format_Cnpj(self):

    # def __str__(self):
    #     if self.tipo_documento == 'cpf':
    #         return self.format_Cpf()
    #     elif self.tipo_documento == 'cnpj':
    #         return self.format_Cnpj()
        

    # def valida_cnpj(self, cnpj):
    #     if len(cnpj) == 14:
    #         validador_cnpj = CNPJ()
    #         return validador_cnpj.validate(cnpj)
    #     else: 
    #         raise ValueError("Quantidade de digitos invalido")