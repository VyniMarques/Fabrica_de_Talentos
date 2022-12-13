# classe Usuario
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.maioridade = self.__testaMarioridade()
        self.periodo = 0

    def __testaMarioridade(self):
        if self.idade >= 18:
            return "Maior"
        else:
            return "Menor"

    def mostraInfo(self):
        print("\nNome: {}".format(self.nome) +
              "\nIdade: {}".format(self.idade) +
              "\nMaioridade: {}".format(self.maioridade))
        self.mostraPeriodo()

    def mudarPeriodo(self, periodo):
        self.periodo = periodo

    def mostraPeriodo(self):
        if self.periodo != 0:
            print("Esta no {} periodo".format(self.periodo))
        else:
            print("Não tem peridodo")

    def mudarPeriodo(self, novo_periodo):
        self.periodo = novo_periodo

    def mudarIdade(self, idade_nova):
        self.idade = idade_nova
        self.maioridade = self.__testaMarioridade()


# fluxo padrão de informações
def menu_principal():
    print("\n____MENU____\n")
    print("1 - Cadastrar novo usuario\n"
          "2 - Verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar usuario\n"
          "5 - Alterar idade\n"
          "6 - Alterar Periodo\n"
          "S - Sair\n")
    return input()


sair = False
lista = []
while sair == False:
    menu = menu_principal()
    objeto = ""
    if menu == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        lista.append(Usuario(nome, idade))
    elif menu == "2":
        for objeto in lista:
            objeto.mostraInfo()
    elif menu == "3":
        objeto = lista[-1]
        print("Nome: {} \n"
              "Idade: {} \n"
              "Maioridade {}".format(objeto.nome, objeto.idade, objeto.maioridade))
    elif menu == "4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "5":
        nome_m = input("Nome: ").capitalize()
        idade_n = int(input("Idade nova: "))
        for objeto in lista:
            if objeto.nome == nome_m:
                objeto.mudarIdade(idade_n)
    elif menu == "6":
        nome_m = input("Nome: ").capitalize()
        periodo_n = input("Periodo novo: ")
        for objeto in lista:
            if objeto.nome == nome_m:
                objeto.mudarPeriodo(periodo_n)
    elif menu.upper() == "S":
        sair = True

print("\nPrograma finalizado")
