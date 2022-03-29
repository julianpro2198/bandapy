from logica.instrumento import Instrumento


class Bajo(Instrumento):
    def tocar(self):
        print("Tocando bajo")
    def afinar(self):
        print("Afinando bajo")
