"""20 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método  aumenta_salario.
Crie duas subclasses da classe funcionário, programador  e  analista, implementando o método  nas duas subclasses.
Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
Depois disso, crie uma classe de testes instanciando os objetos programador e analista e chame o método  aumenta_salario
de cada um."""

class funcionario:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.salario = 0
    def aumenta_salario(self):
        self.salario = self.salario
        #botei isso porque essa daqui não serve pra nada

class programador(funcionario):
    def aumenta_salario(self):
        self.salario = self.salario + 20
        print("Salário do(a) programador(a) após o aumento: %.2f" % (self.salario))

class analista(funcionario):
    def aumenta_salario(self):
        self.salario = self.salario + 30
        print("Salário do(a) analista após o aumento: %.2f" % (self.salario))

class testes:
    def cadastro(self):
        tipo = ""  # tipo de funcionário
        jojo = ""  # variável pra pegar o tipo de funcionário e depois usada como objeto do tipo específico de funcionário
                   # escolhido pelo usuário

        while jojo.lower() != "programador" and jojo.lower() != "programadora" and jojo.lower() != "analista":
            jojo = input("Digite o tipo de funcionário que será cadastrado (programador(a) ou analista):")
            if jojo.lower() != "programador" and jojo.lower() != "programadora" and jojo.lower() != "analista":
                print("Opção inexistente. Tente novamente.")

        if jojo.lower() == "programador" or jojo.lower() == "programadora":
            jojo = programador()
            tipo = "programador(a)"
        elif jojo.lower() == "analista":
            jojo = analista()
            tipo = "analista"

        jojo.nome = input("Digite o nome do(a) %s:" % (tipo))

        while jojo.idade <= 5 or jojo.idade > 120:
            try:
                jojo.idade = int(input("Digite a idade do(a) %s:" % (jojo.nome)))
                if jojo.idade <= 5 or jojo.idade > 120:
                    if jojo.idade <= 5:
                        resposta = "Não temos funcionários tão novos assim!"
                    elif jojo.idade > 130:
                        resposta = "Não temos funcionários tão velhos assim!"
                    print("Valor inválido. %s" % (resposta))
            except ValueError:
                print("Valor inválido.")

        pedro = False
        while pedro == False:
            try:
                jojo.salario = float(input("Digite o salário do/a %s:" % (jojo.nome)))
                pedro = True
                #NOTA IMPORTANTE: Quando se coloca algo embaixo do input do try, esse algo só será executado
                #caso não dê um erro de valor. Se der um erro de valor, ele vai pular diretamente para o comando:
                #"except ValueError:"

            except ValueError:
                print("Valor inválido.")

        jojo.aumenta_salario()

t = testes()
t.cadastro()