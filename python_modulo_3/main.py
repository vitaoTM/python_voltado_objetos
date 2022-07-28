from datetime import datetime
from pytz import timezone
import pytz

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = url.replace(" ", "")

if url == "":
    raise ValueError("A url esta vazia")

url_base = url[0:19]

url_parametros = url[20:36]
interrogacao = url.find('?')

url_parametros = url[interrogacao:]
# print(url_parametros)

parametro_de_busca = "quantidade"
indice_parametros = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametros + len(parametro_de_busca) +1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)