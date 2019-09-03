"""22 - Crie a classe Imóvel, que possui um endereço e um preço.
a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.
b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto.
"""

class imovel():

    def __init__(self):
        self.adicional = 0
        self.endereco = ""
        self.preco = 0

class novo(imovel):

    def __init__(self):
        self.adicional = 10000
        self.preco = self.preco + self.adicional
    def imprimir_adicional(self):
        print("Valor adicional = R$%.2f reais." % self.adicional)
    def preco_atualizado(self):
        return self.preco

class velho(imovel):

    def __init__(self):
        self.adicional = -10000
        self.preco = self.preco + self.adicional
    def imprimir_adicional(self):
        print("Valor do desconto = R$%.2f reais." % self.adicional * -1)
    def preco_atualizado(self):
        return self.preco

class compras:

    def compra(self):
        jojo = imovel()

        jojo.endereco = input("Digite o endereço do imóvel a ser registrado:")

        try:
            jojo.preco = float(input("Digite o preço do imóvel a ser registrado:"))
        except ValueError:
            print("Valor inválido.")

        tipoDeImovel = ""
        while tipoDeImovel.lower() != "novo" and tipoDeImovel.lower() != "velho":
            tipoDeImovel = input("Digite o tipo de imóvel que você pretende registrar (novo ou velho):")
            if tipoDeImovel.lower() != "novo" and tipoDeImovel.lower() != "velho":
                print("Opção inexistente.")

        if tipoDeImovel == "novo":
            jojo = novo()
            batatafrita = "acréscimo"

        else:
            jojo = velho()
            batatafrita = "decréscimo"

        print(jojo.imprimir_adicional())
        print("Valor do imóvel após aplicar o %s de R$%.2f reais: R$%.2f reais." % batatafrita, jojo.adicional, jojo.preco_atualizado())

c = compras()
c.compra()
