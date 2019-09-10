"""27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v    w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um método para "traduzir",
que recebe uma lista com uma mensagem (secreta) e "traduz" a sequência armazenada em uma lista.
"""

from dicionario27 import Hmmm

d = Hmmm()
mensagem = []
joj = 0


def digitar_mensagem():
    op = "não"
    while op.lower() == "não" or op.lower() == "nao":
        hmmm = []
        try:
            pedro = -1
            while pedro > 26 or pedro < 0:
                pedro = int(input("Digite a mensagem secreta. "
                                  "\nDicionário:"
                                  "\n0 = " ", 1 = a, 2 = b, 3 = c, 4 = d, 5 = e, 6 = f, 7 = g, 8 = h, 9 = i,"
                                  "\n10 = j, 11 = k, 12 = l, 13 = m, 14 = n, 15 = o, 16 = p, 17 = q, 18 = r, 19 = s,"
                                  "\n20 = t, 21 = u, 22 = v, 23 = w, 24 = x, 25 = y, 26 = z."))

                hmmm.append(pedro)
                mensagem.append(hmmm[:])
            for i in range(mensagem.__len__()):
                print("Estado atual da mensagem: %s" % d(mensagem[i][0]))
        except ValueError:
            print("Valor inválido.")
        op = "batata frita"
        while op.lower() != "sim" and op.lower() != "não" and op.lower() != 'nao':
            op = input("Deseja digitar mais? (responda com 'sim' ou 'não')")
            if op.lower() != "sim" and op.lower() != "não" and op.lower() != 'nao':
                print("Opção inexistente. Tente novamente.")
    joj = 1


def mostrar_mensagem():
    print("Mensagem:")
    for i in range(mensagem.__len__()):
        print(d(mensagem[i][0]))


def deletar_item():
    print("Mensagem e o número de cada caracter:")
    for i in range(mensagem.__len__()):
        print("%s (%d)" % d(mensagem[i][0]), i)
    try:
        item = int(input("Digite o número do caracter a ser deletado."))
        if item > (mensagem.__len__() - 1) or item < 0:
            print("Opção inexistente.")
    except ValueError:
        print("Valor inválido.")
    mensagem.pop(item)


def refazer_mensagem():
    for i in range(mensagem.__len__()):
        mensagem.pop([i][0])
    joj = 0


def menu():
    op = 0
    if joj == 0:
        try:
            while op != 1 and op != 2:
                op = int(input("MENU DE OPÇÕES:\n1) Digitar mensagem;\n2) Sair."))
                if op != 1 and op != 2:
                    print("Opção inexistente.")
        except ValueError:
            print("Valor inválido.")
        if op == 1:
            digitar_mensagem()
        if op == 2:
            exit()
    else:
        try:
            while op < 1 or op > 4:
                op = int(input("MENU DE OPÇÕES:\n1) Mostrar mensagem;\n2) Deletar caracter;\n3) Refazer mensagem;\n4) Sair."))
                if op < 1 or op > 4:
                    print("Opção inexistente.")
        except ValueError:
            print("Valor inválido.")
        if op == 1:
            mostrar_mensagem()
        elif op == 2:
            deletar_item()
        elif op == 3:
            refazer_mensagem()
        else:
            exit()


menu()
