"""1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não. Receba os dados pela
console e chame este método. (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a média
mostrando se está aprovado ou não)"""


class aluno:
    def __init__(self):
        self.n1 = 0.0
        self.n2 = 0.0
        self.n3 = 0.0
        self.nome = ""
        self.media = 0.0

    def nome_aluno(self):
        self.nome = input("Digite o nome do(a) aluno(a):")


class calculaMedia:
    def med(self):
        pedro = aluno()
        pedro.nome_aluno()
        for i in range(3):
            batata = -1
            while batata < 0 or batata > 10:
                try:
                    batata = int(input("Digite a nota número %d do(a) %s:" % (i+1, pedro.nome)))
                    if batata < 0 or batata > 10:
                        print("Nota inválido. Digite uma nota entre 0 e 10!")
                except ValueError:
                    print("Valor inválido.")
                if i == 0:
                    pedro.n1 = batata
                elif i == 1:
                    pedro.n2 = batata
                elif i == 2:
                    pedro.n3 = batata   
        pedro.media = (pedro.n1 + pedro.n2 + pedro.n3) / 3
        if pedro.media >= 6:
            print("%s está aprovado(a), com uma média igual a %.2f!" % (pedro.nome, pedro.media))
        else:
            print("%s está reprovado(a), com uma média igual a %.2f!" % (pedro.nome, pedro.media))


try:
    numero_alunos = int(input("Digite o número de alunos dos quais as notas serão registradas:"))
except ValueError:
    print("Valor inválido.")

c = calculaMedia()
for i in range(numero_alunos):
    c.med()