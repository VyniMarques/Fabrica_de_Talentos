"""
    - Um sistema que plote no mapa os pontos disponibilizados.
    - O sistema deve ser construido usando classes e funções.
    - As classses criadas devem estar em arquivos separados
"""
import folium
from Ponto import Ponto

file = open("lat_lon.txt", "r")
lista = file.read().split("\n")

lat = lista[0].split(",")
lon = lista[1].split(",")
nome = lista[2].split(",")

if lat[-1] == "":
    lat.pop(-1)
if lon[-1] == "":
    lon.pop(-1)
if nome[-1] == "":
    nome.pop(-1)

if len(lat) == len(lon) == len(nome):
    inatel = [-22.257044861335906, -45.69635809285212]
    mapa = folium.Map(location=inatel, zoom_start=17)

    i = 0
    pontos = []
    for aux in lat:
        pontos.append(Ponto(lat[i], lon[i], nome[i]))
        i += 1

    j = 0
    for auxiliar in pontos:
        pontos[j].marcarPonto(mapa)
        j += 1
    mapa.save("index.html")
    file.close()
else:
    print("Tamanhos diferentes")
