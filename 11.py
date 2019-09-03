"""11 -  Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor."""

try:
    valor = int(input("Digite um número inteiro:"))
except ValueError:
    print("Valor inválido.")

antecessor = valor - 1

print("O antecessor do valor digitado é igual a: %d" % antecessor)
