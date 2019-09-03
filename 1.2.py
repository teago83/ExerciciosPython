"""1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não. Receba os dados pela
console e chame este método. (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a média
mostrando se está aprovado ou não)"""

class aluno:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
    def media(self):
        uhhhh = (self.n1+self.n2+self.n3)/3
        if uhhhh >= 6:
            print("bicho ta aprovado moro")
        else:
            print("ih mlk n foi desa ves")

class calculaMedia:
    def media(self):
        pedro = aluno()
        try:
            pedro.n1 = int(input("digita a n1 dele ae pow"))
        except ValueError:
            print("ih bicho nao rolou nao ein tu digito erado, macimo 10 minimo 0")
        try:
            pedro.n2 = int(input("digita a n2 dele ae pow"))
        except ValueError:
            print("ih bicho nao rolou nao ein tu digito erado, macimo 10 minimo 0")
        try:
            pedro.n3 = int(input("digita a n3 dele ae pow"))
        except ValueError:
            print("ih bicho nao rolou nao ein tu digito erado, macimo 10 minimo 0")
        media = (pedro.n1 + pedro.n2 + pedro.n3)/3
        if media >= 6:
            print("bicho ta aprovado sacou")
        else:
            print("ihh, lascou, rapas")

for i in range (5):
    calculaMedia.media()