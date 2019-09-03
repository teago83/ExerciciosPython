"""24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas, isto é, 1º da 1ª lista, 1º da 2ª lista,
2º da 1ª lista, 2º da 2ª lista."""

lista_1 = []
lista_2 = []

try:
    numero_das_jocas = int(input("Digite o número de elementos que você gostaria de adicionar a ambas as listas:"))
except ValueError:
    print("Valor inválido.")

"""lista = []

for i in range (5):
    auxiliar = []
    nome = input("Digite o nome número %d:" % (i+1))
    auxiliar.append(nome)
    lista.append(auxiliar[:])"""

print("Lista 1:")
for i in range (numero_das_jocas):
    pedro = []
    try:
        joca = float(input("Elemento número %d:" % (i+1)))
        pedro.append(joca)
    except ValueError:
        print("Valor inválido.")
    lista_1.append(pedro[:])

print("Lista 2:")
for i in range (numero_das_jocas):
    pedro = []
    try:
        joca = float(input("Elemento número %d:" % (i + 1)))
        pedro.append(joca)
    except ValueError:
        print("Valor inválido.")
    lista_2.append(pedro[:])

print("União das listas:")
for i in range (numero_das_jocas):
    print("Elemento número %d da união: %.2f" % (i+1, lista_1[i][0]))
for i in range (numero_das_jocas):
    print("Elemento número %d da união: %.2f" % (i+numero_das_jocas+1, lista_2[i][0]))
print("Intercalação das listas:")
for i in range (numero_das_jocas + numero_das_jocas):
    if i % 2 == 0:
        print("Elemento número %d da intercalação: %.2f" % (i+1, lista_1[i][0]))
    elif i % 2 != 0:
        print("Elemento número %d da intercalação: %.2f" % (i+1, lista_2[i][0]))