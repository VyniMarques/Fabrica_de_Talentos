def minha_funcao(entrada_da_funcao):
    return entrada_da_funcao.upper()

nome = input("entre com um nome: ")
novo_nome = minha_funcao(nome)
print(novo_nome)


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


print("=====Cadastrando usuarios=====")
continua = False
lista_usuarios = []
while continua == False:
    lista_usuarios.append(cadastro())
    resp = input("Continuar Cadastrando?(S/N) \n").upper()
    if resp == "S":
        continua = False
    elif resp == "N":
        continua = True
    else:
        print("Resposta invalida!")
        continua = True

for usuario in lista_usuarios:
    print("{} tem {} anos de idade e é {} de idade".format(usuario[0], usuario[1], usuario[2]))

# #Exercicio
# print("=====Cadastrando usuarios=====")
# continua = False
# flag2 = False
# var = []
# while continua == False:
#     while flag2 == False:
#         nome = input("Nome do usuario: \n")
#         idade = int(input("Idade do usuario: \n"))
#         if idade >= 18:
#             maior = True
#             flag2 = True
#         elif 0 < idade < 18:
#             maior = False
#             flag2 = True
#         else:
#             print("Idade invalida!")
#             flag2 = False
#
#     usuario = {"Nome": nome, "Idade": idade, "Maior de idade": maior}
#     var.append(usuario)
#
#     resp = input("Continuar Cadastrando?(S/N) \n")
#     if resp == "S" or resp == "s":
#         continua = False
#         flag2 = False
#     elif resp == "N" or resp == "n":
#         continua = True
#     else:
#         print("Resposta invalida!")
#         continua = True
#
# print(var)





# nome = input("Qual seu nome?\n ")
# idade = int(input("Qual sua idade?\n "))
#
# # print(f"Ola {nome}")
# print("{} tem {} anos de idade".format(nome, idade))
#
# if idade > 18:
#     print("{} é maior de idade".format(nome))
# else:
#     print("{} é menor de idade".format(nome))

# Exercicio