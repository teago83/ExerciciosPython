"""25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade"""

lista = []
hmmm = []

pedro = 0
while pedro < 1 or pedro % 2 != 0:
    try:
        pedro = int(input("Digite o número de elementos que você gostaria de digitar:"
                          "\n(Somente números pares serão aceitos.)"))
        if pedro % 2 != 0:
            print("Você digitou um valor ímpar. Tente novamente.")

    except ValueError:
        print("Valor inválido.")

batata = int(pedro/2)

for i in range (batata):
    alfonse = []
    jorge = input("(%d) Digite o valor desejado." % (i+1))
    alfonse.append(jorge)
    hmmm.append(alfonse[:])


for i in range (batata):
    alfonse = []
    jorge = input("(%d) Digite o valor desejado." % (i+(batata)))
    alfonse.append(jorge)
    lista.append(alfonse[:])

lista.extend(hmmm)

for i in range (pedro):
    print("Valor número %d: %s" % (i+1, lista[i][0]))