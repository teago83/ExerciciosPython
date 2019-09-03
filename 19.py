"""19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos: quantidadeMarchas(); tipoFreio() e marca();
Crie também duas classes que estendem esta classe, uma se chamará BicicletaPasseio e a outra BicicletaProfissional.
Para ﬁnalizar crie uma classe onde deverá estar o método main e crie uma instancia de cada tipo de bicicleta e mostre
o resultado dos métodos."""

class bicicleta:
    def __init__(self):
        self.quantidade_marchas = 4
        self.tipo_freio = "batata"
        self.marca = "frita"

class bicicletaPasseio(bicicleta):
    def __init__(self):
        self.quantidade_marchas = 6
        self.tipo_freio = "arroz"
        self.marca = "samsung"

class bicicletaProfissional(bicicleta):
    def __init__(self):
        self.quantidade_marchas = 8
        self.tipo_freio = "strogonoff"
        self.marca = "semp toshiba"

class piriri:
    def main(self):
        a = bicicleta()
        b = bicicletaPasseio()
        c = bicicletaProfissional()

        print("Bicicleta comum: "
              "\nQuantidade de marchas: %d"
              "\nTipo de freio: %s"
              "\nMarca: %s" % (a.quantidade_marchas, a.tipo_freio, a.marca))
        print("Bicicleta de passeio: "
              "\nQuantidade de marchas: %d"
              "\nTipo de freio: %s"
              "\nMarca: %s" % (b.quantidade_marchas, b.tipo_freio, b.marca))
        print("Bicicleta profissional: "
              "\nQuantidade de marchas: %d"
              "\nTipo de freio: %s"
              "\nMarca: %s" % (c.quantidade_marchas, c.tipo_freio, c.marca))

predo = piriri()
predo.main()