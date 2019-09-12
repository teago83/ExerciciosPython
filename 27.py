"""27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v    w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um método para "traduzir",
que recebe uma lista com uma mensagem (secreta) e "traduz" a sequência armazenada em uma lista.
"""

from Parte1.IsASCII import IsAscII
from Parte1.dicionario27 import Hmmm

d = Hmmm()
check = IsAscII()
mensagem = []
joj = 0


def digitar_mensagem():
    batata = False
    while batata == False:
        mensagem = input("Digite a mensagem a ser traduzida para números.") 
        if check(mensagem) == False:
            batata = False
            print("Valor inválido. Tente novamente. Não use símbolos ou números!")
        else:
            batata = True 
    joj = 1


def mostrar_mensagem():
    print("Mensagem:")
    for i in range(mensagem.__len__()):
        print(d(mensagem[i][0]))


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
    elif joj == 1:
        try:
            while op < 1 or op > 3:
                op = int(input("MENU DE OPÇÕES:\n1) Mostrar mensagem;\n2) Refazer mensagem;\n3) Sair."))
                if op < 1 or op > 3:
                    print("Opção inexistente.")
        except ValueError:
            print("Valor inválido.")
        if op == 1:
            mostrar_mensagem()
        elif op == 2:
            refazer_mensagem()
        elif op == 3:
            exit()


menu()
