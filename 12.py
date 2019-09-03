"""12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles. """

try:
    valor_um = float(input("Digite o primeiro valor:"))
except ValueError:
    print("Valor inválido.")

valor_dois = valor_um

while valor_dois == valor_um:
    batata = True
    try:
        valor_dois = float(input("Digite o segundo valor:"))
    except ValueError:
        print("Valor inválido.")
        batata = False #usei isso pra fazer com que não repetisse a mensagem abaixo caso a pessoa digitasse um valor inválido.
    if valor_um == valor_dois and batata == True:
        print("Não digite números iguais!")

if valor_dois > valor_um:
    print("O segundo valor (%.2f) é maior que o primeiro valor (%.2f)." % (valor_dois, valor_um))
else:
    print("O primeiro valor (%.2f) é maior que o primeiro valor (%.2f)." % (valor_um, valor_dois))