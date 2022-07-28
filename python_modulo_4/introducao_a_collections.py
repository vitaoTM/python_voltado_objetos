from contextlib import ContextDecorator
from tkinter.filedialog import SaveFileDialog


idades = [39, 30, 27, 18]

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self. saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo} <<]"

conta_do_vi = ContaCorrente(42)
print(conta_do_vi)

conta_da_je = ContaCorrente(4750)
conta_da_je.deposita(1000)
print(conta_da_je)

contas = [conta_do_vi, conta_da_je]

for conta in contas:
    print(conta)