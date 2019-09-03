"""2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
Este número deverá variar entre 1 e 5. Se o usuário introduzir um número que não pertença a este intervalo, mostre a frase
“número inválido”."""

op = "sim"

while op.lower() == "sim":
    try:
        numero_normal = int(
            input("Digite o número que desejas ver por extenso. O mesmo deverá estar no intervalo de 1 a 5. "))
    except ValueError:
        print("Valor inválido.")

    if numero_normal == 1:
        print("O número digitado foi: Um")
    elif numero_normal == 2:
        print("O número digitado foi: Dois")
    elif numero_normal == 3:
        print("O número digitado foi: Três")
    elif numero_normal == 4:
        print("O número digitado foi: Quatro")
    elif numero_normal == 5:
        print("O número digitado foi: Cinco")
    else:
        print("Valor inválido.")

    try:
        numero_por_extenso = input(
            "Digite o número que desejas ver normalmente. Deverá estar no mesmo intervalo de antes. ")
    except ValueError:
        print("Valor inválido.")

    if numero_por_extenso.upper() == "UM":
        print("O número digitado foi: 1")
    elif numero_por_extenso.upper() == "DOIS":
        print("O número digitado foi: 2")
    elif numero_por_extenso.upper() == "TRÊS" or numero_por_extenso.upper() == "TRES":
        print("O número digitado foi: 3")
    elif numero_por_extenso.upper() == "QUATRO":
        print("O número digitado foi: 4")
    elif numero_por_extenso.upper() == "CINCO":
        print("O número digitado foi: 5")
    else:
        print("Número inválido/não reconhecido.")

    op = "batata"  # botei essa joça pra fazer entrar no loop abaixo, senão, o código nem perguntaria se quer repetir o processo.

    while op.lower() != "sim":
        op = input("Deseja repetir o processo? Responda com 'sim' ou 'não'.")
        if op.lower() == "nao" or op.lower() == "não":
            exit()
        if op.lower() != "sim":
            print("Valor inválido. Tente novamente.")