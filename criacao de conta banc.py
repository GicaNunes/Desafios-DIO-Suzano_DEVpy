"""
Para ler e escrever dados em Python, utilizamos as seguintes funções:
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.
"""

class ContaBancaria:
    def __init__(self, titular):

        # Inicializa a conta bancária com o nome do titular,
        # saldo 0 e lista para armazenar as operações realizadas

        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        """
        Implementa o método para realizar um depósito,
        adiciona o valor ao saldo e registra a operação
        """
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        """
        Implementa o método para realizar um saque.
        Verifica se há saldo suficiente para o saque
        """
        if self.saldo >= abs(valor):
            self.saldo += valor
            self.operacoes.append(f"{valor}")
        else:
            self.operacoes.append("Saque não permitido")

    def extrato(self):
        """
        Cria o método para exibir o extrato da conta e junta
        as operações no formato correto
        """
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")

# Entrada do nome do titular e das transações
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()
