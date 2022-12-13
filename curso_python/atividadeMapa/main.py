"""
    - Um sistema que plote no mapa os pontos disponibilizados.
    - O sistema deve ser construido usando classes e funções.
    - As classses criadas devem estar em arquivos separados
"""
import folium
from Ponto import Ponto

file = open("lat_lon.txt", "r")
lista1 = file.read().split("\n")  # --> lista1[0] = lat lista[1] = lon lista1[2] = nome

lat = lista1[0].split(",")
lon = lista1[1].split(",")
nome = lista1[2].split(",")

inatel = [-22.257044861335906, -45.69635809285212]

mapa = folium.Map(location=inatel, zoom_start=17)

i = 0
lista_p = []
for auxiliar in lat:
    lista_p.append(Ponto(lat[i], lon[i], nome[i]))
    i += 1

#print(lista_p[1].mostraInfo())
#print(len(lista_p))
j = 0
for auxiliar in lista_p:
    if j < len(lista_p)-1:
        lista_p[j].marcarPonto(mapa)
        j += 1

mapa.save("index.html")
file.close()
