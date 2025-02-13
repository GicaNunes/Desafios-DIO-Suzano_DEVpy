"""
Para ler e escrever dados em Python, utilizamos as seguintes funções:
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.
"""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        # Inicialize a lista de contas
        self.contas = []

    def criar_conta(self, titular, saldo):
        # Crie uma nova conta e adicione à lista de contas
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)

    def listar_contas(self):
        # Liste todas as contas no formato "Titular: R$ Saldo"
        contas_str = ", ".join([f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas])
        print(contas_str)

# Cria uma instância de SistemaBancario
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()
