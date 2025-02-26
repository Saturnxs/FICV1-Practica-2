import time
import os

from utils.formulas import formula_distancia, formula_velocidad_final


def convertir_metros_a_guiones(metros):
    return int(metros / ESCALA_DE_DISTANCIA)


def representar_tren(pos, velocidad, tiempo):
    os.system("cls")
    linea = list("-" * LONGITUD_PISTA_GUIONES)
    tren_pos = convertir_metros_a_guiones(pos)
    parada_pos = convertir_metros_a_guiones(POSICION_PARADA)

    if 0 <= parada_pos < len(linea):
        linea[parada_pos] = "🚏"
    if 0 <= tren_pos < len(linea):
        linea[tren_pos] = "🚆"
    else:
        linea[-1] = "🚆"

    print(f"({tiempo:.0f}s) | Partida " + "".join(linea) + f" ({velocidad:.1f} m/s)")


def main():
    # Variables del tren
    estado = "frenando"
    v_actual = VELOCIDAD_INICIAL
    pos_actual = 0
    tiempo_transcurrido = 0

    # Con esto muestro el tren con la velocidad inicial en la línea
    representar_tren(pos_actual, v_actual, tiempo_transcurrido)
    time.sleep(ESCALA_DE_TIEMPO)

    # Mover el tren en la línea
    while True:
        match estado:
            case "frenando":
                pos_actual += formula_distancia(velocidad_inicial=v_actual, aceleracion=DESACELERACION)
                v_actual = formula_velocidad_final(variable_retorno='vf', velocidad_inicial=v_actual,
                                                   aceleracion=DESACELERACION, tiempo=1)
                tiempo_transcurrido += 1

                if v_actual <= 0:
                    estado = "parado"  # Cambiar el estado a parado
            case "parado":
                print("El tren ha llegado a la estación. Parada de 2 minutos (Sumando 120s).")
                time.sleep(1)  # Esperar 1 segundo para representar la parada de 2 minutos

                tiempo_transcurrido += TIEMPO_EN_PARADA  # Sumar el tiempo de parada al contador
                estado = "acelerando"  # Cambiar el estado a acelerando
            case "acelerando":
                pos_actual += formula_distancia(velocidad_inicial=v_actual, aceleracion=ACELERACION)
                v_actual = formula_velocidad_final(variable_retorno='vf', velocidad_inicial=v_actual,
                                                   aceleracion=ACELERACION, tiempo=1)
                tiempo_transcurrido += 1

                if v_actual >= VELOCIDAD_INICIAL:
                    break  # Terminar la simulación

        representar_tren(pos_actual, v_actual, tiempo_transcurrido)
        time.sleep(ESCALA_DE_TIEMPO)

    # Esto es para que se muestre el tren en la línea al final de la simulación
    representar_tren(DISTANCIA_TOTAL, VELOCIDAD_INICIAL, tiempo_transcurrido)
    print("\nEl tren ha retomado su velocidad inicial de 72 km/h (20 m/s).")


# Constantes de la simulación
DISTANCIA_TOTAL = 600  # Distancia total del recorrido en metros
POSICION_PARADA = 200  # Posición de la parada en metros
TIEMPO_EN_PARADA = 120  # Segundos de parada (2 min)

ESCALA_DE_TIEMPO = 0.5  # 1 segundo en la simulación es igual a 0.5 segundos reales, osea está en x2
ESCALA_DE_DISTANCIA = 10  # 1 guion representa 10m
LONGITUD_PISTA_GUIONES = convertir_metros_a_guiones(DISTANCIA_TOTAL)  # Longitud de la pista en guiones

# Constantes del tren
VELOCIDAD_INICIAL = 20  # Velocidad inicial del tren en m/s
DESACELERACION = -1.0  # Desaceleración del tren (m/s^2)
ACELERACION = 0.5  # Aceleración del tren (m/s^2)

if __name__ == "__main__":
    main()
