"""4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne
o troco a ser dado. (modifique para receber um valor de desconto e subtraia do valor do produto)"""

op = "sim"

while op.lower() == "sim":
    try:
        valor_pago = float(input("Digite o valor que foi dado pelo cliente:"))
    except ValueError:
        print("Valor inválido.")
    try:
        valor_do_produto = float(input("Digite o valor do produto que foi comprado:"))
    except ValueError:
        print("Valor inválido")

    troco = valor_pago - valor_do_produto

    if troco == 0:
        print("O valor pago foi igual ao valor do produto (%.2fR$). Por isso, não haverá troco." % valor_do_produto)
    elif troco < 0:
        print("O valor pago (%.2fR$) é menor do que o valor do produto. Tente novamente." % troco)
    else:
        print("O troco será igual a: %.2fR$" % troco)

    op = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")
