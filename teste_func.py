def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "Titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor 

def saca(conta, valor):
    conta["saldo"] -= valor 

def extrato(conta):
    print(f'Saldo de: {conta["saldo"]}')

