"""7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o menor, número, o maior número,
a soma dos números informados e a média """

numero = []
soma = 0
maior_numero = 0
menor_numero = 999999999999999

op = "sim"

while op.lower() == "sim":
    for i in range(10):
        auxiliar = []
        try:
            batata = float(input("Digite o número %d:" % (i+1)))
            auxiliar.append(batata)
        except ValueError:
            print("Valor inválido.")
        numero.append(auxiliar[:])
        if numero[i][0] > maior_numero:
            maior_numero = numero[i][0]
        if numero[i][0] < menor_numero:
            menor_numero = numero[i][0]
        soma = soma + numero[i][0]

    media = soma / 10

    print("Menor número: %.2f"
          "\nMaior número: %.2f"
          "\nSoma: %.2f"
          "\nMédia: %.2f" % (menor_numero, maior_numero, soma, media))

    op = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")