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
