"""
- Menu com opções
    - Cadastro
    - Mostrar todos usuarios
    - Mostrar ultimo cadastrado
    - Deletar usuario
    - Sair
"""


def cadastro():
    nome = input("Nome do usuario: \n").capitalize()
    idade = int(input("Idade do usuario: \n"))
    if idade >= 18:
        maioridade = "maior"
    elif 0 < idade < 18:
        maioridade = "menor"
    else:
        print("Idade invalida!")
    return [nome, str(idade), maioridade]


def menu():
    print(
        "\n___MENU___\n"
        "1-Cadastrar\n"
        "2-Usuarios cadastrados\n"
        "3-Ultimo cadastrado\n"
        "4-Deletar usuario\n"
        "S-Sair\n"
    )
    resposta = input("")
    return resposta


def listarUsuarios(lista):
    for usuario in lista:
        print("{} - {} - {}".format(usuario[0], usuario[1], usuario[2]))


def mostrarUltimo(lista):
    ultimo_usuario = lista[-1]
    print("{} - {} - {}".format(ultimo_usuario[0],
                                ultimo_usuario[1],
                                ultimo_usuario[2]))


def deletarUsuario(lista, nome):
    i = 0
    for usuario in lista:
        if usuario[0] == nome:
            lista.pop(i)
            return lista
        i += 1
    print("Usuario deletado")


sair = False
lista_usuario = []
while sair == False:
    resposta = menu()
    if resposta == "1":  # Cadastro
        usuario = cadastro()
        lista_usuario.append(usuario)
    elif resposta == "2":  # Mostrar todos os usuarios
        listarUsuarios(lista_usuario)
    elif resposta == "3":  # Mostrar ultimo cadastrado
        mostrarUltimo(lista_usuario)
    elif resposta == "4":  # Deletar usuario
        nome_deletar = input("Usuario a deletar:\n").capitalize()
        lista_usuario = deletarUsuario(lista_usuario, nome_deletar)
    elif resposta.upper() == "S":  # Sair
        sair = True
    else:
        print("Escolha uma opção correta!\n")

listarUsuarios(lista_usuario)
