"""30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens."""

dic_a = {
    "Pedro": 15,
    "Japs": 24,
    "Endzó": "???",
    "Teaguis": 83,
    "BorendaPortatile": "Dzim"
    }

dic_b = {
    0: 0,
    0: 0,
    0: 0,
    0: 0,
    0: 0
    }   


#Method to use in order to print the values in a dictionary in the way that you want to print them.
#for k,v in d.items():
#    print(k, 'corresponds to', v)


print("Valores do primeiro dicionário:")
for nome, idade in dic_a.items():
    print("Nome: ", nome, "Idade: ", idade)

print("Valores do segundo dicionário:")
for nome, idade in dic_b.items():
    print("Nome: ", nome, "Idade: ", idade)

dic_b = dic_a.copy()

print("Valores atualizados do segundo dicionário (cópia do primeiro):")
for nome, idade in dic_b.items():
    print("Nome: ", nome, "Idade: ", idade)
