from xml.etree.ElementInclude import LimitedRecursiveIncludeError


class Conta: 
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
        
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do Titular {self.__titular}')

    def deposita(self, valor):
        self.saldo += valor 

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor de {valor} nao pode ser sacado')
            
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
         return self.__titular
    
    def get_saldo(self):
         return self.__saldo
    
    @property 
    def limite(self):
         return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

# static methots
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': "001",
                'Caixa': "104",
                'Bradesco': "237"
                }