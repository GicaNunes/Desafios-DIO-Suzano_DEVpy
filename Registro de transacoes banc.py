"""
Para ler e escrever dados em Python, utilizamos as seguintes funções:
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.
"""

def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista:
    for transacao in transacoes:
        # Adicione o valor da transação ao saldo
        saldo += transacao

    # Retorna o saldo formatado em moeda brasileira com duas casas decimais:
    return f"Saldo: R$ {saldo:.2f}"

entrada_usuario = input().strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)
