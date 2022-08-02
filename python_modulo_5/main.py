# from validate_docbr import CPF

from cpf_cnpj import Documento

cpf_um = "04165893919"

documento = Documento.cria_documento(cpf_um)
print(documento)
# obj_cpf = Cpf(cpf)

cnpj_um = "35379838000112"

documento = Documento.cria_documento(cnpj_um)

print(documento)



