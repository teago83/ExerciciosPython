"""1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não. Receba os dados pela 
console e chame este método. (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a média 
mostrando se está aprovado ou não)"""

jorge = 1

class pessoa: 

    def __init__(self):
        self.idade = 0

    def maior_idade(self, idade):
        if self.idade > 17:
            print("veinho, ja ta com %.f ano" % self.idade)
        elif self.idade < 0:
            print("transcendeu, tem %.f ano mano" % self.idade)
        else:
            print("ih maluco o bicho n eh maior nao, tem so %.f anus kkkkjjjjj" % self.idade)

joj = pessoa()

while jorge == 1 or jorge == 3:
    try:
        joj.idade = float(input("quale tua idade bicho"))
    except ValueError:
        print("ih carai, sa idade nu exist")
    joj.maior_idade(joj.idade)

    jorge = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while jorge.lower() != "sim":
        jorge = input("vai quere continua o n doido (responde ae com sim o nao.")
        if jorge.lower() == "nao" or jorge.lower() == "não":
            exit()
        if jorge.lower() != "sim":
            print("Valor inválido. Tente novamente.")