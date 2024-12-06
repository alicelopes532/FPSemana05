class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(1)
        else:
            print(0)

    def levantar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(1)
        else:
            print(0)

    def exibir_saldo(self):
        print(round(self.saldo, 2))

    def exibir_info(self):
        print(f"{self.titular} {round(self.saldo, 2)} {round(self.limite, 2)}")

# Teste com os dados de exemplo
conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)  # Imprime 0
conta.depositar(500.00)   # Imprime 1
conta.levantar(1200.00)   # Imprime 1
conta.levantar(1200.00)   # Imprime 0
conta.exibir_info()        # Imprime: "João 300.00 500.00"
