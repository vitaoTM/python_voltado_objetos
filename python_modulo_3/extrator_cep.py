import re
endereco = "Rua Ione Stolf Januzelli 56, Paulinia, Sao Paulo, 13148-064"
telefone = "+ 55 (19) 99367-1971"

padrao_tel = re.compile("[+]{0,1}[0123456789]")

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)