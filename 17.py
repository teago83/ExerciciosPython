"""17 - Crie uma lista para armazenar 5 nomes fixos. Após inserir os 5 nomes da lista mostre-os no console (utilize um for)."""

lista = []

for i in range (5):
    auxiliar = []
    nome = input("Digite o nome número %d:" % (i+1))
    auxiliar.append(nome)
    lista.append(auxiliar[:])

print("Lista de nomes registrados:")

for i in range (5):
    print("Nome número %d: %s" % (i+1, lista[i][0]))