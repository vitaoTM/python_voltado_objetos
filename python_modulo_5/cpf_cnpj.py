# from validate_doctor import CPF, CNPJ

# class Documento:
#     @staticmethod
#     def cria_doc(documento):
#         if len

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido")

    def __str__(self):
        return self.format_Cpf()

    def valida_cpf(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_Cpf(self):
        fatia_um = self.cpf[:3]    
        fatia_dois = self.cpf[3:6] 
        fatia_tres = self.cpf[6:9] 
        fatia_quatro = self.cpf[9:]
        return f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}"
        