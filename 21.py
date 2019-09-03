"""21 - Crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor().
a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).
b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".
c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIP
"""

class ingresso:
    def __init__(self):
        self.valor = 100
    def imprimeValor(self):
        return self.valor

class VIP(ingresso):
    def __init__(self):
        self.local = ""
    def aumentaValor(self):
        self.valor = self.valor + 50

class normal(ingresso):
    def ingressoNormal(self):
        return "ingresso normal"

class camaroteInferior(VIP):
    def __init__(self):
        self.taxa = 0
        self.local = "camarote inferior"
    def valorFinal(self):
        self.aumentaValor()
        self.valor = self.valor + self.taxa

class camaroteSuperior(VIP):
    def __init__(self):
        self.taxa = 50
        self.local = "camarote superior"
    def valorFinal(self):
        self.aumentaValor()
        self.valor = self.valor + self.taxa

class compraDeIngresso:
    def compra(self):
        tipoDeIngresso = ""
        while tipoDeIngresso.lower() != "normal" and tipoDeIngresso.lower() != "vip":
            tipoDeIngresso = input("Digite o tipo de ingresso desejado (normal ou VIP):")
            if tipoDeIngresso.lower() != "normal" and tipoDeIngresso.lower() != "vip":
                print("Opção inexistente.")

        if tipoDeIngresso.lower() == "normal":
            jojo = normal()
            print("Você acabou de comprar um %s. O valor da compra foi de R$%d reais." % (jojo.ingressoNormal(), jojo.imprimeValor()))

        elif tipoDeIngresso.lower() == "vip":
            jojo = VIP()
            while jojo.local.lower() != "inferior" and jojo.local.lower() != "superior":
                try:
                    jojo.local = input("Digite o camarote onde você vai querer estar durante a festa (inferior ou superior):")
                    if jojo.local.lower() != "inferior" and jojo.local.lower() != "superior":
                        print("Opção inexistente.")
                except ValueError:
                    print("Valor inválido.")
            if jojo.local.lower() == "inferior":
                jojo = camaroteInferior()
            elif jojo.local.lower() == "superior":
                jojo = camaroteSuperior()
            print("Você acabou de comprar um ingresso VIP no %s."
                  "\nTaxa: R$%d reais."
                  "\nValor total: R$%d reais." % jojo.local, jojo.taxa, jojo.valorFinal())

c = compraDeIngresso()
c.compra()