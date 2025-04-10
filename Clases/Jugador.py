class Jugador:
    def __init__ (self, nombre : str, genero : str, equipo : list):
        self.nombre : str = nombre
        self.genero : str = genero
        self.__equipo : list = equipo

    def mostrar_jugador(self):
        ...

