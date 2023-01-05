import random

class player:
    #### Definimos la clase jugador

    def __init__(self):
    #### Definimos las propiedades iniciales
        self.score=0
        self.opciones={0:"Piedra", 1:"Papel",2:"Tijera"}
        self.eleccion=0

    #### Definimos 3 metodos para la clase:'elegir','elegirAzar','sumarpunto'
    def elegir(self):
        print(self.opciones)
        self.eleccion=int(input("Elige una opción para jugar: "))

    def elegirAzar(self):
        keys=list(self.opciones.keys())
        self.eleccion=random.choice(keys)

    def sumarpunto(self):
        self.score += 1

def comparar(player_one,player_two):
    ##### Definimos la funcion comparar, la cual sirve para comparar entre las elecciones del jugador
    dif=player_one.eleccion-player_two.eleccion
    if dif ==1 or dif ==-2:
        player_one.sumarpunto()
    elif dif ==-1 or dif ==2:
        player_two.sumarpunto()
    else:
        print("Empate")

def juego(jugador_uno,jugador_dos,numero_puntos, numero_jugadores):
    ####El juego se desarrolla hasta que uno de los dos jugadores obtenga el puntaje

    while ((jugador_uno.score < numero_puntos) and (jugador_dos.score < numero_puntos)):
        ####Dependiendo del numero de jugadores es la opcion para jugador_dos
        if numero_jugadores == 0:
            jugador_uno.elegirAzar()
            jugador_dos.elegirAzar()
        elif numero_jugadores == 1:
            jugador_uno.elegir()
            jugador_dos.elegirAzar()
        else:
            jugador_uno.elegir()
            jugador_dos.elegir()

        comparar(jugador_uno,jugador_dos)
        print("El jugador uno eligió:", jugador_uno.opciones[jugador_uno.eleccion])
        print("El jugador dos eligió:", jugador_dos.opciones[jugador_dos.eleccion])
        print("El marcador va:", jugador_uno.score, "vs", jugador_dos.score)

    ####Obtenido el puntaje, muestra cual jugador ganó
    if jugador_uno.score>jugador_dos.score:
        print("#" * 50)
        print("Ganó el jugador 1")
    else:
        print("#" * 50)
        print("Ganó el jugador 2")

def main():
    ##### Definimos la funcion principal que inicia el juego

    ##### Iniciamos creando dos objetos 'player'
    jugador_uno = player()
    jugador_dos = player()

    ##### Solicitamos el numero de jugadores y el numero de puntos a los que se van a jugar
    numero_jugadores = int(input("Cuántos jugadores? \n"))
    numero_puntos = int(input("A cuantos puntos vamos a jugar? \n"))

    #### Iniciamos el juego
    juego(jugador_uno,jugador_dos,numero_puntos,numero_jugadores)

    ###### Estas lineas son para preguntar si el jugador desea seguir jugando.
    jugar_otra_vez=int(input("Quieres volver a jugar? 1. Si, 2, No. \n"))
    if jugar_otra_vez == 1:
        main()
    else:
        print("Gracias por jugar.")
        exit()

#################################################################################
############Para asegurar que el juego se ejecute de manera directa##############

if __name__ == '__main__':
    main()
