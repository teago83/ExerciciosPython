"""27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v    w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um método para "traduzir",
que recebe uma lista com uma mensagem (secreta) e "traduz" a sequência armazenada em uma lista.
"""

from 27dicionario import Dicionario

d = Dicionario()

mensagem = []
op = "não"
while op == "não" or op == "nao":
    try:
        pedro = -1
        while pedro > 26 or pedro < 0:
            pedro = int(input("Digite o número desejado."))

        for i in range (mensagem.__len__()):
            print(mensagem[i][0])
    except ValueError:
        print("Valor inválido.")


"""mensagem = int(input("Digite a mensagem secreta. "
                             "\nDicionário:"
                             "\n0 = " ", 1 = a, 2 = b, 3 = c, 4 = d, 5 = e, 6 = f, 7 = g, 8 = h, 9 = i,"
                             "\n10 = j, 11 = k, 12 = l, 13 = m, 14 = n, 15 = o, 16 = p, 17 = q, 18 = r, 19 = s,"
                             "\n20 = t, 21 = u, 22 = v, 23 = w, 24 = x, 25 = y, 26 = z."))"""
