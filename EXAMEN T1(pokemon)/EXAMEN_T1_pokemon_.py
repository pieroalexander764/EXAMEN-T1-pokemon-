import random

# -----------------------------
# Clase Entrenador
# -----------------------------
class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre


# -----------------------------
# Clase Pokemon
# -----------------------------
class Pokemon:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.max_vida = random.randint(150, 400)
        self.vida_actual = self.max_vida

    def recuperar(self):
        """Recupera la vida al máximo"""
        self.vida_actual = self.max_vida


# -----------------------------
# Variables globales
# -----------------------------
entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None
ganadas = 0
perdidas = 0


# -----------------------------
# Funciones solicitadas
# -----------------------------
def crearEntrenadorPokemon(n):
    global entrenador1, pokemon1, entrenador2, pokemon2
    nombre_entrenador = input(f"Ingrese el nombre del entrenador {n}: ")
    nombre_pokemon = input(f"Ingrese el nombre del pokemon del entrenador {n}: ")

    if n == 1:
        entrenador1 = Entrenador(nombre_entrenador)
        pokemon1 = Pokemon(nombre_pokemon)
        print(f"\n--> Su pokemon {pokemon1.nombre} ha sido creado con:")
        print(f"Ataque máximo: {pokemon1.max_ataque}")
        print(f"Vida máxima: {pokemon1.max_vida}\n")
    else:
        entrenador2 = Entrenador(nombre_entrenador)
        pokemon2 = Pokemon(nombre_pokemon)
        print(f"\n--> El pokemon rival {pokemon2.nombre} ha sido creado con:")
        print(f"Ataque máximo: {pokemon2.max_ataque}")
        print(f"Vida máxima: {pokemon2.max_vida}\n")


def valorDeAtaque(n):
    if n == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)


def defender(n, valor_ataque):
    dado = random.randint(1, 6)
    if dado == 6:  # Defensa perfecta
        valor_ataque = 0

    if n == 1:
        pokemon1.vida_actual -= valor_ataque
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual -= valor_ataque
        return pokemon2.vida_actual


# -----------------------------
# Programa principal
# -----------------------------
def main():
    global ganadas, perdidas

    print("=== BIENVENIDO A POKEMON BATTLE ===")
    crearEntrenadorPokemon(1)  # Creación del jugador principal

    while True:
        print("\nMenú:")
        print("P - Pelear")
        print("F - Finalizar")
        opcion = input("Seleccione una opción: ").upper()

        if opcion == "P":
            crearEntrenadorPokemon(2)
            # Recuperar vida antes de pelear
            pokemon1.recuperar()
            pokemon2.recuperar()

            print("\n--- ¡COMIENZA LA BATALLA! ---")
            turno = 1  # Siempre empieza el jugador

            while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
                if turno == 1:
                    ataque = valorDeAtaque(1)
                    vida_restante = defender(2, ataque)
                    print(f"{entrenador1.nombre} ({pokemon1.nombre}) ataca con {ataque} puntos.")
                    print(f"{pokemon2.nombre} queda con {max(vida_restante,0)} de vida.\n")
                    turno = 2
                else:
                    ataque = valorDeAtaque(2)
                    vida_restante = defender(1, ataque)
                    print(f"{entrenador2.nombre} ({pokemon2.nombre}) ataca con {ataque} puntos.")
                    print(f"{pokemon1.nombre} queda con {max(vida_restante,0)} de vida.\n")
                    turno = 1

            # Resultado de la pelea
            if pokemon1.vida_actual > 0:
                print(f"\n🏆 ¡Ganó {entrenador1.nombre} con {pokemon1.nombre}!")
                ganadas += 1
            else:
                print(f"\n💀 Ganó {entrenador2.nombre} con {pokemon2.nombre}.")
                perdidas += 1

        elif opcion == "F":
            print("\n=== FIN DEL JUEGO ===")
            print(f"Entrenador: {entrenador1.nombre}")
            print(f"Pokemon: {pokemon1.nombre}")
            print(f"Ataque máximo: {pokemon1.max_ataque}")
            print(f"Vida máxima: {pokemon1.max_vida}")
            print(f"Encuentros ganados: {ganadas}")
            print(f"Encuentros perdidos: {perdidas}")
            break
        else:
            print("Opción inválida, intente de nuevo.")


# -----------------------------
# Ejecutar
# -----------------------------
if __name__ == "__main__":
    main()

