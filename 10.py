"""10 - receba três notas de um aluno e informe se ele passou ou reprovou."""

class aluno:
    def __init__(self):
        self.nota = -1
        self.soma = 0
        self.media = 0
        self.numeroDeNotas = 0

    def cadastrar_nota(self):
        while self.nota > 10 or self.nota < 0:
            try:
                self.nota = float(input("Digite a nota do aluno:"))
            except ValueError:
                print("Valor inválido.")
            if self.nota > 10 or self.nota < 0:
                print("Nota inválida. Digite uma nota maior ou igual a 0 ou menor ou igual a 10.")
        self.numeroDeNotas = self.numeroDeNotas + 1
        self.soma = self.soma + self.nota

    def calcular_media(self):
        self.media = self.soma/self.numeroDeNotas
        return self.media

predo = aluno()

def menu():
    op = "batata"

    while op.lower() != "sim":
        op = input("Deseja registrar uma nota? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            if predo.numeroDeNotas < 1:
                batata = True
                exit()
            else:
                print("A média do aluno é igual a: %.2f" % (predo.calcular_media()))
                if predo.calcular_media() >= 6:
                    print("O aluno foi aprovado.")
                else:
                    print("O aluno foi reprovado.")
                batata = True
                exit()
        elif op.lower() == "sim":
            predo.cadastrar_nota()
        else:
            print("Valor inválido. Tente novamente.")

batata = False
while batata == False:
    menu()