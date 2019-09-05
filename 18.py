"""18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo".
Depois disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal come.
Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o método comer polimorficamente
(com um for)"""


class Animal:
    def comer(self):
        print("O animal está comendo.")


class Cachorro(Animal):
    def comer(self):
        print("O cachorro está comendo whiskas sachê.")


class Cavalo(Animal):
    def comer(self):
        print("O cavalo está comendo mato.")


class Gato(Animal):
    def comer(self):
        print("O gato está comendo ração.")


d = Cachorro()
h = Cavalo()
c = Gato()


class AnimalTeste:
    def arroz(self):
        for i in range(3):
            if i == 0:
                d.comer()
            if i == 1:
                h.comer()
            if i == 2:
                c.comer()


pedro = AnimalTeste()


pedro.arroz()
