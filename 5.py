"""5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo), se é par ou ímpar """

op = "sim"

while op.lower() == "sim":
    try:
        valor = int(input("Digite o valor que gostarás de saber se é positivo ou negativo e se é par ou ímpar:"))
    except ValueError:
        print("Valor inválido.")

    if valor < 0:
        uhhh = "negativo"
    else:
        uhhh = "positivo"
    if valor % 2 == 0:
        hmmm = "par"
    else:
        hmmm = "ímpar"

    print("O valor digitado é %s. É um número %s" % (uhhh, hmmm))

    op = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")