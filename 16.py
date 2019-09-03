"""16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de uma caixa retangular.
Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA"""

try:
    comprimento = float(input("Digite o comprimento da caixa (em cm):"))
except ValueError:
    print("Valor inválido.")

try:
    largura = float(input("Digite a largura da caixa (em cm):"))
except ValueError:
    print("Valor inválido.")

try:
    altura = float(input("Digite a altura da caixa (em cm):"))
except ValueError:
    print("Valor inválido.")

print("O volume da caixa equivale a: %.2f cm³" % (comprimento * largura * altura))