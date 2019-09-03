"""15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles. """

valores = []
maior_valor = 0

class valor:
    def __init__(self):
        self.value = 0

class cadastroValor:
    def cadastro(self):
        auxiliar = []
        valorrr = valor()
        pedro = False
        while pedro == False:
            try:
                batata = int(input("Digite o valor número %d:" % (i+1)))
                if batata not in valores:
                    valorrr.value = batata
                    auxiliar.append(batata)
                    pedro = True
                else:
                    print("Valor já digitado anteriormente. Tente novamente.")
            except ValueError:
                print("Valor inválido.")
        valores.append(auxiliar[:])

cadastro = cadastroValor()

for i in range (10):
    cadastro.cadastro()

for i in range (10):
    if valores[i][0] > maior_valor:
        maior_valor = valores[i][0]

print("Maior valor equivale a: %d" % maior_valor)