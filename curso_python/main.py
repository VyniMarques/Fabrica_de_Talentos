# f = open("meu_primeiro_arquivo.txt", "w")
# f.write("Minha primeira frase\n")
# f.write("Minha segunda frase\n")
# f.write("Minha terceira frase\n")
# f.close()
#
# file = open("files/clubes.txt", "r")
# clubes = file.read().split("\n")
# print(type(clubes))
# file.close()

#abrindo o arquivo como READ and WRITE
f = open("files\clubes_pts.txt", "r+")
# separando cada linha
lista = f.read().split("\n")
nova_lista = []
# Separando o nome do clube com o nome da
for auxiliar in lista:
    time = auxiliar.split(" - ")
    nova_lista.append(time)
# Ordenando a nova
nova_lista.sort(key= lambda x: x[1], reverse=True)

for index, time in enumerate(nova_lista):
    string = "em {}º lugar temos {} com {} pontos".format((index + 1), time[0], time[1])
    print(string)
    f.write(string + "\n")
f.close()

import folium

class Ponto:
    def __init__(self, lat, lon, nome):
        self.lat = lat
        self.lon = lon
        self.nome = nome

    def marcarPonto(self, mapa):
        lat_lon = str(self.lat + self.lon)
        popup_text = self.nome
        tooltip_text = "Clique aqui"
        folium.Marker(location=lat_lon, popup=popup_text, tooltip=tooltip_text).add_to(mapa)
