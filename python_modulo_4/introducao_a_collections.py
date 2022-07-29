from contextlib import ContextDecorator
from msilib.schema import Class
from tkinter.filedialog import SaveFileDialog
import array as arr
import numpy as np


idades = [39, 30, 27, 18]
class Conta:
    def __init__(self, codigo ):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo {self._codigo} Saldo {self._saldo} <<]"

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo} <<]"

    def deposita_para_contas(contas):
        for conta in contas:
            conta.deposita(100)


conta_do_vi = ContaCorrente(42)

conta_da_je = ContaCorrente(4750)
conta_da_je.deposita(1000)

contas = [conta_do_vi, conta_da_je]

for conta in contas:
    print(conta)