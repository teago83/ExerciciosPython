"""9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase."""

try:
    x = int(input("Digite o número de vezes que você vai querer ver a oração 'ZA WARUDO!' na tela."))
except ValueError:
    print("Valor inválido.")

for i in range (x):
    print("ZA WARUDO! (%d)" %(i + 1))