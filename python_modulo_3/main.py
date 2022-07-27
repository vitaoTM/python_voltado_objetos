from datetime import datetime
from pytz import timezone
import pytz

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url_base = url[0:19]

url_parametros = url[20:36]
interrogacao = url.find('?')

url_parametros = url[interrogacao:]
# print(url_parametros)

parametro_de_busca = "moedaOrigem"
indice_parametros = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametros + len(parametro_de_busca) +1
valor = url_parametros[indice_valor:]

print(valor)