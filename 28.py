"""28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista. 
Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5"""

class hmmmmmmmmm():
    def __init__(self):
        self.joj = 0
        self.lista = []
        self.media = 0.0

    def cria_lista(self):
        self.joj = 1
        try:
            pedro = int(input("Digite o tamanho desejado para a lista."))
        except ValueError:
            print("Valor inválido.")
        try:
           for i in range(pedro):
            hmmm = []
            batata = float(input("Digite o valor numérico %d:" %(i+1)))
            hmmm.append(batata)
        except ValueError:
            print("Valor inválido.")
        self.lista.append(batata[:])


    def define_media(self):
        arroz = 0.0
        for i in range(self.lista.__len__):
            arroz = arroz + self.lista[i][0]
        self.media = arroz/self.lista.__len__


    #Method to check closest number to a given value:
    #min(myList, key=lambda x:abs(x-myNumber))
    def checa_proximidade(self, mutilo):
        predo = min(self.lista, key=lambda x:abs(x-mutilo))
        print("Valor da lista mais próximo ao digitado é: %.2f" %(predo))


    def valor_proximo(self):
        try:
            valor = float(input("Digite o número desejado para checar o mais próximo a ele na lista."))
        except ValueError:
            print("Valor inválido.")
        return valor


hm = hmmmmmmmmm()

def menu():
    if hm.joj == 0:
        hm.cria_lista
    if hm.joj == 1:
        op = 0
        while op < 1 or op > 3:
            try:
                op = int(input("MENU DE OPÇÕES:\n1) Definir valor desejado para checar qual é o valor mais próximo dele da lista;\n2) Refazer lista;\n3) Sair."))
                if op < 1 or op > 3:
                    print("Opção inexistente. Tente novamente.")
            except ValueError:
                print("Valor inválido.")
            if op == 1:
                hm.define_media
                hm.checa_proximidade(hm.valor_proximo)

menu()