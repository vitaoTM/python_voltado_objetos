"""
Verifica se a base da URL está de acordo com o padrão correto.
"""
import re

url = 'https://bytebank.com/cambio'


padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é valida")
print("a URL é valida")