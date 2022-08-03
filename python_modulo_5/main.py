# from validate_docbr import CPF
from datetime import datetime
from telefones_br import TelefonesBr
from cpf_cnpj import Documento
from datas import DatasBr
from numpy import piecewise
# padrao de data Br dd/mm/yyyy


cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)

# telefone = "433343-2255"

# tel_obj = TelefonesBr(telefone)
# padrao = "\w{1,50}.\w{1,50}@\w{2,3}.\w{2,3}"

# texto = "ahdjaof oasjoajsoa soa oajs aohfpa vitor.grosskof@gmail.com"
# resposta = re.search(padrao, texto)

# print(resposta.group())




# cpf_um = "04165893919"

# documento = Documento.cria_documento(cpf_um)
# print(documento)
# # obj_cpf = Cpf(cpf)

# cnpj_um = "35379838000112"

# documento = Documento.cria_documento(cnpj_um)

# print(documento)



