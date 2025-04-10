class Pokemon:
    
    def __init__(self, nombre, puntos_salud, puntos_ataque, puntos_defensa):
        self.nombre = nombre,
        self.puntos_salud = puntos_salud
        self.__puntos_ataque = puntos_ataque
        self.__puntos_defensa = puntos_defensa