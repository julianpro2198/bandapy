from logica.instrumento import Instrumento


class Musico():
    
    def tocar(self):
        self.instrumento.tocar()

    def asignar_instrumento(self, instrumento):
        self.instrumento = instrumento
    