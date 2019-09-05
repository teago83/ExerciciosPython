"""26 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrário,
além do número de ocorrências do primeiro elemento da lista."""

primeiro_elemento_a = "a"
primeiro_elemento_b = "b"
lista_a = []
lista_b = []
pedro = 0  # contador pra fazer as magias no loop final e ver se os números são todos iguais
ocorrencias_primeiro_a = 0  # contador de ocorrencias do primeiro elemento da lista 'a'
ocorrencias_primeiro_b = 0  # mesmo que o de cima, só que para a lista 'b'.

batata = False
while batata == False:
    try:
        numero = int(input("Digite o número de elementos que ambas as listas terão:"))
        batata = True
    except ValueError:
        print("Valor inválido.")

for i in range(numero):
    auxiliar = []
    hmmm = input("Digite o elemento número %d a ser adicionado à primeira lista." % (i+1))
    auxiliar.append(hmmm)
    lista_a.append(auxiliar[:])
    if i == 0:
        primeiro_elemento_a = hmmm

for i in range(numero):
    auxiliar = []
    hmmm = input("Digite o elemento número %d a ser adicionado à segunda lista." % (i+1))
    auxiliar.append(hmmm)
    lista_b.append(auxiliar[:])
    if i == 0:
        primeiro_elemento_b = hmmm

for i in range(numero):
    if lista_a[i][0] != lista_b[i][0]:
        pedro = pedro + 1
    if lista_a[i][0] == primeiro_elemento_a:
        ocorrencias_primeiro_a = ocorrencias_primeiro_a + 1
    if lista_a[i][0] == primeiro_elemento_b:
        ocorrencias_primeiro_b = ocorrencias_primeiro_b + 1
    if lista_b[i][0] == primeiro_elemento_a:
        ocorrencias_primeiro_a = ocorrencias_primeiro_a + 1
    if lista_b[i][0] == primeiro_elemento_b:
        ocorrencias_primeiro_b = ocorrencias_primeiro_b + 1

if pedro > 0:
    print(False)
else:
    print(True)

print("Número de ocorrências do primeiro elemento da primeira lista: %d" % ocorrencias_primeiro_a)
print("Número de ocorrências do primeiro elemento da segunda lista: %d" % ocorrencias_primeiro_b)
