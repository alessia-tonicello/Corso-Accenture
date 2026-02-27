class ContoBancario:

    def __init__(self, saldo):
        self._saldo = saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):
        if 0 < importo < self._saldo:
            self._saldo -= importo

    def mostra_saldo(self):
        return self._saldo

# utilizzando un _ proteggiamo
# se utilizziamo due __ nascondiamo il saldo




conto_di_ciccio = ContoBancario(10000)

conto_di_ciccio.deposita(100)
conto_di_ciccio.preleva(1000)

print(conto_di_ciccio.mostra_saldo)