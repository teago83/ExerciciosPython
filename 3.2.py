"""3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações. (modifique para calcular tudo
no mesmo método, somando 1 ao resultado de cada operação)"""

op = "sim"

class calculadora:

    def __init__(self):
        x = 0
        y = 0

    def conta(self, x, y):
        print("Resultado das contas:"
              "\nSoma: %.2f"
              "\nSubtração: %.2f"
              "\nMultiplicação: %.2f"
              "\nDivisão: %.2f" %(x + y, x - y, x * y, x / y))

batata = calculadora()

def operacao():
    try:
        xis = float(input("Digite o primeiro número:"))
    except ValueError:
        print("Valor inválido.")

    try:
        ispu = float(input("Digite o segundo número:"))
    except ValueError:
        print("Valor inválido.")

    batata.conta(xis, ispu)

    op = "batata" #botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")

while op.lower() == "sim":
    operacao()