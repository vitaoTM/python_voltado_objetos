# from validate_docbr import CPF

from cpf_cnpj import Cpf_Cnpj

cpf_um = Cpf_Cnpj("04165893919", 'cpf')
print(cpf_um)
# obj_cpf = Cpf(cpf)

cnpj_um = "35379838000112"

documento = Cpf_Cnpj(cnpj_um, 'cnpj')

print(documento)



