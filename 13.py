"""13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre
diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
e o produto das idades do homem mais novo com a mulher mais velha."""

idadesHomi = []
idadesMuie = []

class cadastroHomem:
    def cadastroMan(self):
        auxiliar = []
        pedro = False
        while pedro == False:
            try:
                batata = int(input("Digite a idade do homem número %d:" % (i+1)))
                if batata not in idadesHomi:
                    auxiliar.append(batata)
                    print("Idade registrada: %d" % batata)
                    pedro = True
                elif batata in idadesHomi:
                    print("Idade já registrada!")
            except ValueError:
                print("Valor inválido.")
        idadesHomi.append(auxiliar[:])

class cadastroMulher:
    def cadastroWoman(self):
        auxiliar = []
        pedro = False
        while pedro == False:
            try:
                batata = int(input("Digite a idade da mulher número %d:" % (i+1)))
                if batata not in idadesMuie:
                    auxiliar.append(batata)
                    print("Idade registrada: %d" % batata)
                    pedro = True
                elif batata in idadesMuie:
                    print("Idade já registrada!")
            except ValueError:
                print("Valor inválido.")
        idadesMuie.append(auxiliar[:])

homi_mais_novo = 99999999999999
muie_mais_nova = 99999999999999
homi_mais_veio = 0
muie_mais_veia = 0

a = cadastroHomem()
b = cadastroMulher()

for i in range (2):
    a.cadastroMan()

for i in range (2):
    b.cadastroWoman()

for i in range (2):
    print(idadesHomi[i][0])

for i in range (2):
    print(idadesMuie[i][0])

"""for i in range (2):
    a.cadastroMan()
    if idadesHomi[i][0] > homi_mais_veio:
        homi_mais_veio = idadesHomi[i][0]
    if idadesHomi[i][0] < homi_mais_novo:
        homi_mais_novo = idadesHomi[i][0]

for i in range (2):
    b.cadastroWoman()
    if idadesMuie[i][0] > muie_mais_veia:
        muie_mais_veia = idadesMuie[i][0]
    if idadesMuie[i][0] < muie_mais_nova:
        muie_mais_nova = idadesMuie[i][0]

print("Soma da idade do homem mais velho com a idade da mulher mais nova: %d anos." % (homi_mais_veio + muie_mais_nova))
print("Produto da multiplicação da idade do homem mais novo com a idade da mulher mais velha: %d anos." % (homi_mais_novo * muie_mais_veia))"""