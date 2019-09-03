class calculadora():
    def soma(self, x, y):
        return x + y
    def subtracao(self, x, y):
        return x - y
    def multiplicacao(self, x, y):
        return x * y
    def divisao(self, x, y):
        return x / y

calc = calculadora()

def menu():

    while True:
        try:
            op = int(input("1) Soma"
                           "\n2) Subtração"
                           "\n3) Multiplicação"
                           "\n4) Divisão"
                           "\n5) Vazar"
                           "\nDigite a operação desejada."))
        except ValueError:
            print("Valor inválido.")
        break

    xis = int(input("Digite o valor número 1:"))
    ispu = int(input("Digite o valor número 2:"))

    if op == 1:
        print("Resultado da soma: %d" %(calc.soma(xis, ispu)))
    elif op == 2:
        print("Resultado da subtração: %d" % (calc.subtracao(xis, ispu)))
    elif op == 3:
        print("Resultado da multiplicação: %d" % (calc.multiplicacao(xis, ispu)))
    elif op == 4:
        print("Resultado da divisão: %d" % (calc.divisao(xis, ispu)))
    elif op == 5:
        exit()

while True:
    menu()


