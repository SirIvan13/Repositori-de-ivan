class CuentaBancaria:
    def __init__(self,balance,cvu):
        self.cvu = cvu
        self.balance = balance

    def depositar(self,monto):
        self.balance += monto

    def transferir(self,monto,cuenta_destino):
        self.balance -= monto
        cuenta_destino.depositar(monto)

    def __str__(self):
        resulta2 = ("{} {}").format(self.balance, self.cvu)
        return resulta2


cuenta_origen = CuentaBancaria(0,"CVU de Juan")
cuenta_dif = CuentaBancaria(0,"CVU de Juan't")
print(dir(cuenta_origen))
print(cuenta_dif)