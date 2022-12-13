import folium


class Ponto:
    def __init__(self, lat, lon, nome):
        self.lat = lat
        self.lon = lon
        self.nome = nome

    def marcarPonto(self, mapa):
        lat_lon = (self.lat, self.lon)
        tooltip_text = "Clique aqui"
        folium.Marker(location=lat_lon, popup=self.nome, tooltip=tooltip_text).add_to(mapa)

    def mostraInfo(self):
        print("Nome: {}\n"
              "Latitude: {}\n"
              "Longitude: {}\n".format(self.nome, self.lat, self.lon))
