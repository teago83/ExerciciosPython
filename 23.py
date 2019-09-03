"""23 - Crie um programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos
"""

import random

soma = 0
lista = []
ocorrenciasUm = 0
maiorNumero = 0

for i in range (15):
    auxiliar = []
    batata = random.randint(0, 10)
    auxiliar.append(batata)
    if i > 0 and batata in lista:
        ocorrenciasUm = ocorrenciasUm + 1
    lista.append(auxiliar[:])
    soma = soma + batata
    if batata > maiorNumero:
        maiorNumero = batata

print("Valores da lista:")

for i in range (15):
    print("Valor número %d: %d" % (i+1, lista[i][0]))

print("Maior número: %d"
      "\nSoma dos elementos: %d"
      "\nNúmero de ocorrências do primeiro elemento: %d"
      "\nMédia dos elementos: %.2f" % (maiorNumero, soma, ocorrenciasUm, soma/15))
