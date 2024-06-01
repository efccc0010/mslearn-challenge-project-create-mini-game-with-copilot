""" 
Juego de Piedra, Papel y Tijeras.

Contexto:
Se tiene dos jugadores (una persona y el ordenador) los cuales pueden escoger entre
Piedra, Papel y Tijeras, donde en cada ronda jugada se
sabe quien ganó, perdió o empató. Para pasar a una siguiente 
ronda se deberá escoger si desea continuar jugando o no. Al finalizar 
debe salir los puntajes de cada jugador y el mensaje de quien ganó.

Reglas del juego:
    - Piedra gana a Tijeras
    - Tijeras gana a Papel
    - Papel gana a Piedra
    - Cada ronda ganada suma 1 punto al jugador ganador

Codigo:
    - Una funcion que tenga la logica del juego, esta debe retornar si el jugador gano, perdio o empato (string)
    - Un Enum para las opciones de juego
    - En una funcion main se llama a la funcion del juego y se imprime el resultado
    - La opcion de ordenador es un aleatorio
    - El jugador debe ingresar su opcion
"""
from enum import Enum
import random


class Opciones(Enum):
    PIEDRA = "piedra"
    PAPEL = "papel"
    TIJERAS = "tijeras"

    def ganador(self, opcion):
        if self == opcion:
            return "empate"
        if self == Opciones.PIEDRA:
            return "gana" if opcion == Opciones.TIJERAS else "pierde"
        if self == Opciones.PAPEL:
            return "gana" if opcion == Opciones.PIEDRA else "pierde"
        if self == Opciones.TIJERAS:
            return "gana" if opcion == Opciones.PAPEL else "pierde"


def juego(opcion):
    opciones = list(Opciones)
    opcion_pc = random.choice(opciones)
    return opcion_pc.ganador(opcion)

# Agregar un logica (while) en el main que pregunte si desea continuar jugando
# Donde la opcion 1 es continuar y la opcion 2 es salir
def main():
    continuar = 's'
    puntos_jugador = 0
    puntos_pc = 0
    total_rondas = 0
    while continuar == 's':
        print("Juego de Piedra, Papel y Tijeras")
        jugador = input("Ingrese su opcion (piedra, papel, tijeras): ").lower()
        while jugador not in ['piedra', 'papel', 'tijeras']:
            print("Opción no válida. Por favor, ingrese piedra, papel o tijeras.")
            jugador = input("Ingrese su opcion (piedra, papel, tijeras): ").lower()
        opcion = Opciones(jugador)
        resultado = juego(opcion)
        if resultado == 'gana':
            puntos_jugador += 1
        elif resultado == 'pierde':
            puntos_pc += 1
        print(f"El jugador {resultado}")
        total_rondas += 1
        continuar = input("¿Desea continuar jugando? (s/n): ").lower()
    print(f"Total de rondas jugadas: {total_rondas}")
    print(f"Puntos finales - Jugador: {puntos_jugador}, PC: {puntos_pc}")

if __name__ == "__main__":
    main()