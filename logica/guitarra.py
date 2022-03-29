from logica.instrumento import Instrumento


class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando guitarra")
    def afinar(self):
        print("Afinando guitarra")
