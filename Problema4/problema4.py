import math

from utils.formulas import formula_distancia


def main():
    print("\nEste programa cálcula la la separación y tiempos de dos vehiculos que se encuentran a cierta "
          "distancia y se mueven el uno hacia el otro durante 3 segundos.\n")

    distancia_separacion = float(input("Distancia de separación entre los vehículos en metros (0.0): "))
    aceleracion_carro1 = float(input("Aceleración del carro 1 en m/s^2 (0.0): "))
    aceleracion_carro2 = float(input("Aceleración del carro 2 en m/s^2 (0.0): "))

    # Separación de los vehículos luego de 3 segundos

    distancia_carro1 = formula_distancia('d', aceleracion=aceleracion_carro1, distancia=distancia_separacion, tiempo=TIEMPO_SEGUNDOS)
    distancia_carro2 = formula_distancia('d', aceleracion=aceleracion_carro2, distancia=distancia_separacion, tiempo=TIEMPO_SEGUNDOS)

    distancia_recorrida = distancia_separacion - distancia_carro1 - distancia_carro2

    if distancia_recorrida > 0:
        print(f"\nLuego de {TIEMPO_SEGUNDOS} segundos los vehículos están a {distancia_recorrida} metros de toparse.")
    elif distancia_recorrida < 0:
        print(
            f"\nLuego de {TIEMPO_SEGUNDOS} segundos los vehículos se rebasaron mutuamente y están a una distancia de {abs(distancia_recorrida)} metros.")
    else:
        print(f"\nLuego de {TIEMPO_SEGUNDOS} segundos los vehículos se encuentran en el mismo punto.")

    # Tiempo en que se topan los vehículos (distancia_recorrida = distancia_vehiculo_1 + distancia_vehiculo_2)
    tiempo = math.sqrt(distancia_separacion/(0.5*(aceleracion_carro1 + aceleracion_carro2)))
    tiempo = round(tiempo, 3)

    print(f"\nEl tiempo desde que los vehiculos arrancan hasta que se topan es de {tiempo} segundos.")


TIEMPO_SEGUNDOS = 3


if __name__ == "__main__":
    main()
