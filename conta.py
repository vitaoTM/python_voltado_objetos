class Conta: 
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo de {self.saldo} do Titular {self.titular}')

    def deposita(self, valor):
        self.saldo += valor 

    def saca(self, valor):
        self.saldo -= valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
         return self.__titular
    
    def get_saldo(self):
         return self.__saldo
    
    def get_limite(self):
         return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
