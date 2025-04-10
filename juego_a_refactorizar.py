from Clases.Jugador import *
from Clases.Pokemon import *
from Clases.Rival import Rival

generos_permitidos_para_el_jugador : list = ['CHICO', 'CHICA', "MASCULINO", "FEMENINO", "HOMBRE", "MUJER"]
pokemons_iniciales : list = ['CHARMANDER','SQUIRTLE', 'BULBASAUR']
rival = Rival("Joaquin", "Masculino", [])

puntos : int = 0
cantidad : int = 1


def Punto_Ganado(cantidad):
    global puntos
    puntos += cantidad


'''
TAREA:

Encontrar un método para que el algoritmo elija al pokemon del jugador y en base a lo excluido elija al del rival.

'''
# def eleccion_de_pokemon_jugador_rival(pokemon):
#     if pokemon == 1:
#         print("Asi que CHARMANDER! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
#         mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
#         if mote_pokemon is not None or '':
#             pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
#         pokemon_elegido_por_jugador = Pokemon("Charmander", 100, 25, 12)
#         #Excluye al pokemon de la eleccion del rival
#         pokemon_excluido_por_rival = pokemon 
#     if pokemon == 2:
#         print("Asi que SQUIRTLE! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
#         mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
#         if mote_pokemon is not None or '':
#             pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
#         pokemon_elegido_por_jugador = Pokemon("Squirtle", 100, 25, 12)
#     pokemon_excluido_por_rival = pokemon
#     if pokemon == 3:
#         print("Asi que BULBASAUR! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
#         mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
#         if mote_pokemon is not None or '':
#             pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
#         pokemon_elegido_por_jugador = Pokemon("Bulbasaur", 100, 25, 12)
#         pokemon_excluido_por_rival = pokemon



import random


#Dialogos principales del juego
print("¡Hola! ¡Éste es el mundo de POKÉMON!\n\
¡Me llamo ALONSO! ¡Pero la gente me llama PROFESOR ALONSOMON!\n\
PROF. ALONSOMON: ¡Éste mundo está habitado por unas criaturas llamadas POKÉMON!\n\
PROF. ALONSOMON: Para algunos, los POKÉMON son mascotas. Pero otros los usan para pelear.\n\
PROF. ALONSOMON: En cuanto a mí... Estudio a los POKÉMON como profesión.")

#Preguntas 1
print("PROF. ALONSOMON: Bueno, cuéntame algo de ti.")
genero_jugador = str(input("¿Eres chico o chica?: ")).upper()

while genero_jugador not in generos_permitidos_para_el_jugador:
    print(f"Lo siento no entendi bien, porfavor ingresa una de las opciones validas...")
    genero_jugador = str(input(f"{generos_permitidos_para_el_jugador}: ").upper())

if genero_jugador in generos_permitidos_para_el_jugador:
    print(f"Oh, eres {genero_jugador}! que bien.")

nombre = str(input("Ahora dime tu nombre: "))
print(f"¡Bien!\n\
¡Asi que te llamas {nombre}!")

print(f"PROF. ALONSOMON: Este es mi nieto, Joaquin.\n\
PROF. ALONSOMON: Ha sido tu rival desde que eran pequenos.\n\
PROF. ALONSOMON: {nombre}! Tu propia leyenda POKEMON esta a punto de comenzar!\n\
PROF. ALONSOMON: Te espera un mundo de suenos y aventuras con los POKEMON!\n\
Adelante!")

jugador = Jugador(nombre, genero_jugador, [])

#Toma de decisiones 1
print('*Despiertas en tu cama* Que quieres hacer?')
accion1 = int(input("Ir con mama (1) o salir de casa (2)"))
while accion1 not in [1, 2]:
    print("Lo siento, ingresa una opcion valida.")
    accion1 = int((input("Ir con mama (1) o salir de casa (2) ")))
if accion1 == '1':
    print("MAMA: En fin... Todos los ninos se van de casa algun dia. Asi es la vida! Ah, nuestro vecino, el PROF. ALONSOMON, queria verte.")
else:
    print("*Sales de casa*")

print("*Vas camino fuera de la ciudad cuando te detiene el PROF. ALONSOMON*\n\
PROF. ALONSOMON: Eh! Alto! No te vayas! Cuidado en la hierba viven POKEMON salvajes! Necesitas a tu propio POKEMON como proteccion! Vente conmigo, anda!\n\
*Llegas al laboratorio del PROF. ALONSOMON*")



#Eleccion Pokemon
print(f"Joaquin: Abuelo! Estoy harto de esperar!\n\
'PROF. ALONSOMON: Joaquin? Dejame pensar... Ah, si! Te pedi que vinieras. Espera... {nombre}, toma! Aqui hay 3 POKEMON! Bien! Estan dentro de las POKE BALLS! Cuando yo era joven, era un buen ENTRENADOR de POKEMON! Pero ahora solo me quedan 3. Te dare uno. Cual quieres?\n\
Joaquin: Oye abuelo! Y yo que?\n\
PROF. ALONSOMON: Tranquilo, Joaquin! Te dare otra a ti!")

pokemon = int(input("Selecciona una opcion Charmander (1), Squirtle (2), Bulbasaur (3): "))
while pokemon not in [1, 2, 3]:
    print("Lo siento, ingresa una opcion valida.")
    pokemon = int(input("Charmander (1), Squirtle (2), Bulbasaur (3): "))
if pokemon == 1:
    print("Asi que CHARMANDER! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
    mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
    if mote_pokemon is not None or '':
        pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
    pokemon_elegido_por_jugador = Pokemon("Charmander", 100, 25, 12)
    #Excluye al pokemon de la eleccion del rival
    pokemon_excluido_por_rival = pokemon 
if pokemon == 2:
    print("Asi que SQUIRTLE! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
    mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
    if mote_pokemon is not None or '':
        pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
    pokemon_elegido_por_jugador = Pokemon("Squirtle", 100, 25, 12)
    pokemon_excluido_por_rival = pokemon
if pokemon == 3:
    print("Asi que BULBASAUR! Pues ten paciencia con el. Ese POKEMON tiene mucha energia.")
    mote_pokemon : str = input("Dale un mote a tu pokemon (deja en blanco si no quieres.): ")
    if mote_pokemon is not None or '':
        pokemon_elegido_por_jugador = Pokemon(mote_pokemon, 100, 25, 12)    
    pokemon_elegido_por_jugador = Pokemon("Bulbasaur", 100, 25, 12)
    pokemon_excluido_por_rival = pokemon

# TODO: Agregar pokemon a la propiedad equipo del JUGADOR.

# Generacion random de eleccion del pokemon del rival
pokemon_rival = random.randint(1,3)
while pokemon_rival == pokemon_excluido_por_rival:
    pokemon_rival = random.randint(1,3)
if pokemon_rival == 1:
    print("JOAQUIN: He escogido un Charmander!")
    pokemon_elegido_por_rival = Pokemon("Charmander", 100, 25, 12)
if pokemon_rival == 2:
    print("JOAQUIN: He escogido un Squirtle!")
    pokemon_elegido_por_rival = Pokemon("Squirtle", 100, 25, 12)
if pokemon_rival == 3:
    print("JOAQUIN: He escogido un Bulbasaur!")
    pokemon_elegido_por_rival = Pokemon("Bulbasaur", 100, 25, 12)

# TODO: Agregar pokemon a la propiedad equipo del rival


print("Joaquin: Pues este para mi\n\
*Joaquin recibio el BULBASAUR de manos del PROF. ALONSOMON*\n\
Joaquin: Espera, {nombre}! Probemos a nuestros POKEMON!\n\
Adelante, luchemos!")



#Pelea 1
Bulbasaur = {"nombre": "Bulbasaur",  "puntos_vida": 100, "ataque": 30, "defensa": 10}
p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
def atacar(atacante, defensor):
    dano = atacante["ataque"] - defensor["defensa"]
    if dano < 0:
        dano = 0
    defensor["puntos_vida"] -= dano
    print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
print("¡Comienza la batalla!")
turno = random.choice([Bulbasaur, p1])
print(f"{turno['nombre']} comienza el combate.")
while Bulbasaur["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
    print(f"{turno['nombre']}, es tu turno de atacar.")
    if turno == Bulbasaur:
        atacar(Bulbasaur, p1)
        turno = p1
    else:
        atacar(p1, Bulbasaur)
        turno = Bulbasaur
    print(f"{Bulbasaur['nombre']} tiene {Bulbasaur['puntos_vida']} puntos de vida restantes.")
    print(f"{p1['nombre']} tiene {p1['puntos_vida']} puntos de vida restantes.")
if Bulbasaur["puntos_vida"] > 0:
    print(f"{Bulbasaur['nombre']} ha ganado la pelea.")
    print(f'*{Npokemon} se a debilitado, mientras sanara en el laboratorio*')
else:
    print("Derrotaste a rival JOAQUIN!")
    print("JOAQUIN: Que?! Increible! Tu POKEMON es mejor que el mio!")
    print("JOAQUIN: Vale! Hare luchar a mi POKEMON para fortalecerlo!")
    Punto_Ganado(1)

#Mision 1
print(f'PROF. ALONSOMON: {nombre}, necesito que me ayudes con un encargo en la tienda de la CIUDAD VERDE.')


#Toma de decisiones 2
accion2 = input("Quieres explorar el pueblo (1) o marchas hacia la ciudad verde (2)? ")
while accion2 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion2 = input("Quieres explorar el pueblo (1) o marchas hacia la ciudad verde (2)? ")
if accion2 == '1':
    print("*Das vueltas por el pueblo, pero lo unico interesante es un charco en el que te reflejas*")
    print("*Marchas hacia la ciudad verde, por la mision del PROF. ALONSOMON*")
else:
    print("*Marchas hacia la ciudad verde, por la mision del PROF. ALONSOMON*")


#Toma de decisiones 3
print("*Un tronco obstruye el camino*")
accion3 = input("Deseas usar corte?\n\
                Si (1)\n\
                No(2) ")
while accion3 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion3 = input("Deseas usar corte?\n\
                Si (1)\n\
                No (2) ")
if accion3 == '1':
    print("*Es superefectivo! Lograste abrirte paso!")
    print("Recoges el encargo del PROF. ALONSOMON en la tienda")
else:
    print("*Podrias buscar otro camino*")
    print("*Tardaste mas de la cuenta y ya es de noche, esperas a que abran la tienda para completar la mision")
    print("*Recoges el encargo del PROF. ALONSOMON en la tienda")


#Pelea 2
print("*Vas regreso al laboratorio del PROF. ALONSOMON, cuando te topas con un Rattata salvaje*")
Rattata = {"nombre": "Rattata",  "puntos_vida": 100, "ataque": 20, "defensa": 10}
p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
def atacar(atacante, defensor):
    dano = atacante["ataque"] - defensor["defensa"]
    if dano < 0:
        dano = 0
    defensor["puntos_vida"] -= dano
    print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
print("¡Comienza la batalla!")
turno = random.choice([Rattata, p1])
print(f"{turno['nombre']} comienza el combate.")
while Rattata["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
    print(f"{turno['nombre']}, es tu turno de atacar.")
    if turno == Rattata:
        atacar(Rattata, p1)
        turno = p1
    else:
        atacar(p1, Rattata)
        turno = Rattata
    print(f"{Rattata['nombre']} tiene {Rattata['puntos_vida']} puntos de vida restantes.")
    print(f"{p1['nombre']} tiene {p1['puntos_vida']} puntos de vida restantes.")
if Rattata["puntos_vida"] > 0:
    print(f"{Rattata['nombre']} ha ganado la pelea.")
    print(f'*{Npokemon} se a debilitado, corres hacia el centro pokemon*')
else:
    print("Rattata enemigo se debilito! Ganas la batalla!")
    Punto_Ganado(1)

print("*Llegas al laboratorio del PROF. ALONSOMON*")
print(f'PROF. ALONSOMON: {nombre}! Como va tu pokemon?\n\
      Creo que te quiere mucho!\n\
      Pareces ser muy habil entrenando POKEMON!\n\
      Tienes mi encargo?')
print("JOAQUIN: ABUELO!\n\
      Que quieres de mi?")
print("PROF. ALONSOMON: Tengan 5 POKEBALLS para cada uno, capturen POKEMONS para formar un equipo.\n\
      Me gustaria hacerlo yo, pero ya estoy muy viejo.\n\
      Adelante, id en su busca!\n\
      Sera una gran proeza en la historia de los POKEMON!")
print("JOAQUIN: No te preocupes abuelo!\n\
      No necesito tu ayuda!\n\
      Le pedire a mi hermana su MAPA!\n\
      Y le dire que no te de ninguno a ti! Ja, ja, ja!")

#Toma de decisiones 4
print("*Sales del laboratorio y te pica la curiosidad de ir a pedir el mapa*")
accion4 = input("Vas a por el mapa a casa de Joaquin?\n\
                Si (1)\n\
                No (2) ")
while accion4 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion4 = input("Vas a por el mapa a casa de Joaquin?\n\
                Si (1)\n\
                No (2) ")
if accion4 == '1':
    print(f'*Vas a casa de Joaquin a pedir un MAPA*\n\
          DALIA: Te encargo algo el abuelo?\n\
          Toma esto!\n\
          Te ayudara!\n\
          *{nombre} recibio el MAPA de manos de DALIA!*\n\
          *Vas hacia la ciudad verde*')

else:
    print("*Avanzas hacia la ciudad verde*")

#Pelea 3
print(f'*En medio de la hierba te topas con algo*\n\
      *Un Pidgey salvaje!*\n\
      {nombre}: Adelante, {Npokemon}!')

accion5 = input("Luchar (1) Huir (2)? ")
while accion5 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion5 = input("Luchar (1) Huir (2)? ")
if accion5 == '1':
    Pidgey = {"nombre": "Pidgey", "puntos_vida": 100, "ataque": 20, "defensa": 10}
    p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
    def atacar(atacante, defensor):
        dano = atacante["ataque"] - defensor["defensa"]
        if dano < 0:
            dano = 0
        defensor["puntos_vida"] -= dano
        print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
    print("¡Comienza la batalla!")
    turno = random.choice([Pidgey, p1])
    print(f'{turno["nombre"]} comienza el combate.')
    while Pidgey["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
        print(f'{turno["nombre"]}, es tu turno de atacar.')
        if turno == Pidgey:
            atacar(Pidgey, p1)
            turno = p1
        else:
            atacar(p1, Pidgey)
            turno = Pidgey
        print(f'{Pidgey["nombre"]} le quedan {Pidgey["puntos_vida"]} puntos de vida restantes.')
        print(f'{p1["nombre"]} le quedan {p1["puntos_vida"]} puntos de vida restantes.')
    if Pidgey["puntos_vida"] > 0:
        print(f'{Pidgey["nombre"]} ha ganado la batalla.')
        print(f'*{Npokemon} se ha debilitado, corres hacia un centro pokemon*')
    else:
        print("Pidgey enemigo se ha debilitado! Ganas la batalla!")
        Punto_Ganado(1)
else:
    print("*Huyes con exito, que cobarde*")

print("*Llegas a la ciudad verde y exploras un poco mas a fondo, cuando escuchas un grito que te parece familiar*")
print(f'Eh! {nombre}!\n\
      *Pero si es Joaquin, que pesado*\n\Vas a la liga POKEMON?\n\
          Joaquin: Olvidalo! Seguro que no tienes ninguna MEDALLA!\n\
              Seguro el guardia no te dejara pasar!\n\
                  Dime, ya son mas fuertes tus POKEMON?')

#Pelea 4
Bulbasaur = {"nombre": "Bulbasaur",  "puntos_vida": 100, "ataque": 30, "defensa": 10}
p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
def atacar(atacante, defensor):
    dano = atacante["ataque"] - defensor["defensa"]
    if dano < 0:
        dano = 0
    defensor["puntos_vida"] -= dano
    print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
print("¡Comienza la batalla!")
turno = random.choice([Bulbasaur, p1])
print(f"{turno['nombre']} comienza el combate.")
while Bulbasaur["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
    print(f"{turno['nombre']}, es tu turno de atacar.")
    if turno == Bulbasaur:
        atacar(Bulbasaur, p1)
        turno = p1
    else:
        atacar(p1, Bulbasaur)
        turno = Bulbasaur
    print(f"{Bulbasaur['nombre']} tiene {Bulbasaur['puntos_vida']} puntos de vida restantes.")
    print(f"{p1['nombre']} tiene {p1['puntos_vida']} puntos de vida restantes.")
if Bulbasaur["puntos_vida"] > 0:
    print(f"{Bulbasaur['nombre']} ha ganado la pelea.")
    print(f'*{Npokemon} se a debilitado, corres hacia un centro POKEMON*')
else:
    print("Joaquin: Derrotaste a Bulbasaur, ahora sigue Pidgey!")
    Punto_Ganado(1)
    
    Pidgey = {"nombre": "Pidgey", "puntos_vida": 100, "ataque": 20, "defensa": 10}
    p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
    def atacar(atacante, defensor):
        dano = atacante["ataque"] - defensor["defensa"]
        if dano < 0:
            dano = 0
        defensor["puntos_vida"] -= dano
        print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
    print("¡Comienza la batalla!")
    turno = random.choice([Pidgey, p1])
    print(f'{turno["nombre"]} comienza el combate.')
    while Pidgey["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
        print(f'{turno["nombre"]}, es tu turno de atacar.')
        if turno == Pidgey:
            atacar(Pidgey, p1)
            turno = p1
        else:
            atacar(p1, Pidgey)
            turno = Pidgey
        print(f'{Pidgey["nombre"]} le quedan {Pidgey["puntos_vida"]} puntos de vida restantes.')
        print(f'{p1["nombre"]} le quedan {p1["puntos_vida"]} puntos de vida restantes.')
    if Pidgey["puntos_vida"] > 0:
        print(f'{Pidgey["nombre"]} ha ganado la batalla.')
        print(f'*{Npokemon} se ha debilitado, corres hacia un centro pokemon*')
    else:
        print("Joaquin: Auuu! Has tenido mucha suerte!")
        Punto_Ganado(1)
        
print("Joaquin: Dicen que los ENTRENADORES de la LIGA POKEMON son muy fuertes!\n\
      Tengo que buscar la forma de vencerles! Deja de perder el timepo y muevete!")
print("Señor mayor: Eh chico! Como vas con tus POKEMON?\n\
      Solo tienes uno? Como? Que no sabes atrapar POKEMON?\n\
          Pues haber empezado por ahi!")
          
print("*Señor mayor abre su mochila*\n\
      Mira esto es una POKEBALL, con ella puedes atrapar mas POKEMON, guardalas en tu mochila.\n\
          *Señor mayor se aporxima hacia un Weedle*\n\
              Señor mayor: Ya que las guardas en tu mochila, cuando quieras atrapar a un POKEMON usa la opcion mochila.\n\
                  Solo puedes usar las POKEBALL sobre POKEMON salvajes, los entrenadores no dejaran que toques a sus POKEMON.")

print("Continuas tu viaje por la RUTA 2 y llegas a la entrada del BOSQUE VERDE, decides entrar*")
print(f'{nombre}: Wow hay mucha hierva por aqui, deben haber un monton de POKEMON por ahi!')

#Pelea 5
accion6 = input("Luchar (1) Huir (2) Mochila (3) ")
while accion6 not in ['1', '2', '3']:
    print("Lo siento, ingresa una opcion valida.")
    accion6 = input("Luchar (1) Huir (2) Mochila (3)")
if accion6 == '1':
    Pikachu = {"nombre": "Pikachu", "puntos_vida": 100, "ataque": 20, "defensa": 10}
    p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
    def atacar(atacante, defensor):
        dano = atacante["ataque"] - defensor["defensa"]
        if dano < 0:
            dano = 0
        defensor["puntos_vida"] -= dano
        print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
    print("¡Comienza la batalla!")
    turno = random.choice([Pikachu, p1])
    print(f'{turno["nombre"]} comienza el combate.')
    while Pikachu["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
        print(f'{turno["nombre"]}, es tu turno de atacar.')
        if turno == Pikachu:
            atacar(Pikachu, p1)
            turno = p1
        else:
            atacar(p1, Pikachu)
            turno = Pikachu
        print(f'{p1["nombre"]} le quedan {p1["puntos_vida"]} puntos de vida restantes.')
    if Pikachu["puntos_vida"] > 0:
        print(f'{Pikachu["nombre"]} ha ganado la batalla.')
        print(f'*{Npokemon} se ha debilitado, corres hacia un centro pokemon*')
    else:
        print("Pikachu enemigo se ha debilitado! Ganas la batalla!")
        Punto_Ganado(1)

elif accion6 == '2':  
  print("Huyes con exito, que cobarde.")

else:
  accion7 = input("Dentro de la mochila solo tienes una Pokeball, quieres usarla? Si (1) No (2) ")
  uno = {"captura": "Pikachu fue capturado con exito."}
  dos = {"captura": "Pikachu escapo, no te quedan mas POKEBALLS."}
  while accion7 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion7 = input("Dentro de la mochila solo tienes una Pokeball, quieres usarla? Si (1) No (2) ")
    if accion7 == '1':
        Pokeball = random.choice([uno, dos])
        print(f'{Pokeball["captura"]}')

    else:
        print("Demoraste tanto que el POKEMON escapo.")

print("*Sales del BOSQUE VERDE ileso.*")
print("*Llegas a CIUDAD PLATEADA*")
print("*Adentrandote en el pueblo te encuentras con un gimnasio POKEMON*")
print("*Te acercas al gimnasio*")
print("*Una persona se acerca a ti*")
print("Alto ahí, enclenque!")
print("¡Todavia estas a anos luz de derrotar a BROCK! ")


#Penultima pelea
accion8 = input("Luchar (1) Huir (2) ")
while accion8 not in ['1', '2']:
    print("Lo siento, ingresa una opcion valida.")
    accion8 = input("Luchar (1) Huir (2) ")
if accion8 == '1':
    Geodude = {"nombre": "Geodude", "puntos_vida": 100, "ataque": 20, "defensa": 10}
    p1 = {"nombre": {Npokemon}, "puntos_vida": 100, "ataque": 30, "defensa": 10}
    def atacar(atacante, defensor):
        dano = atacante["ataque"] - defensor["defensa"]
        if dano < 0:
            dano = 0
        defensor["puntos_vida"] -= dano
        print(f"{atacante['nombre']} ha hecho {dano} puntos de daño a {defensor['nombre']}.")
    print("¡Comienza la batalla!")
    turno = random.choice([Geodude, p1])
    print(f'{turno["nombre"]} comienza el combate.')
    while Geodude["puntos_vida"] > 0 and p1["puntos_vida"] > 0:
        print(f'{turno["nombre"]}, es tu turno de atacar.')
        if turno == Geodude:
            atacar(Geodude, p1)
            turno = p1
        else:
            atacar(p1, Geodude)
            turno = Geodude
        print(f'{p1["nombre"]} le quedan {p1["puntos_vida"]} puntos de vida restantes.')
    if Geodude["puntos_vida"] > 0:
        print(f'{Geodude["nombre"]} ha ganado la batalla.')
        print(f'*{Npokemon} se ha debilitado, corres hacia un centro pokemon*')
    else:
        print("Pikachu enemigo se ha debilitado! Ganas la batalla!")
        Punto_Ganado(1)

print(f"{nombre}, tu puntuación final es: {puntos}")