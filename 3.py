"""3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações. (modifique para calcular tudo
no mesmo método, somando 1 ao resultado de cada operação)"""

op = "sim"

class calculadora:

    def __init__(self):
        x = 0
        y = 0

    def soma(self, x, y):
        return x + y
    def subtracao(self, x, y):
        return x - y
    def multiplicacao(self, x, y):
        return x * y
    def divisao(self, x, y):
        return x / y

batata = calculadora()

def operacao():
    try:
        op = input("Digite a operação desejada (soma, subtração, multiplicação ou divisão):")
    except ValueError:
        print("Opção inválida.")

    try:
        xis = float(input("Digite o primeiro número:"))
    except ValueError:
        print("Valor inválido.")

    try:
        ispu = float(input("Digite o segundo número:"))
    except ValueError:
        print("Valor inválido.")

    if op.lower() == "soma":
        print("Resultado da soma: %.2f" % batata.soma(xis, ispu))
    if op.lower() == "subtracao" or op.lower() == "subtração":
        print("Resultado da subtração: %.2f" % batata.subtracao(xis, ispu))
    if op.lower() == "multiplicacao" or op.lower() == "multiplicacão" or op.lower() == "multiplicação" or op.lower() == "multiplicação":
        print("Resultado da multiplicação: %.2f" % batata.multiplicacao(xis, ispu))
    if op.lower() == "divisao" or op.lower() == "divisão":
        print("Resultado da divisão: %.2f" % batata.divisao(xis, ispu))

    op = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")

while op.lower() == "sim":
    operacao()
