class CuentaBancaria:
    def __init__(self,balance,cvu):
        self.cvu = cvu
        self.__balance = balance

    def depositar(self,monto):
        self.__balance += monto

    def transferir(self,monto,cuenta_destino):
        self.__balance -= monto
        cuenta_destino.depositar(monto)



cuenta_origen = CuentaBancaria(0,"CVU de Juan")
cuenta_dif = CuentaBancaria(0,"CVU de Juan't")
print(dir(cuenta_origen))
cuenta_origen._CuentaBancaria__balance = 12
print(cuenta_dif)