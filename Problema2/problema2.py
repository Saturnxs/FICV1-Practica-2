from utils.formulas import formula_velocidad
from utils.conversiones import meses_a_dias, meses_a_semanas, meses_a_anios


def main():
    print("\nEste programa cálcula el tiempo que tarda en crecer el peso desde una longitud inicial hasta una longitud "
          "final\n")

    longitud_inicial = float(input("Longitud inicial del pelo en centímetros (0.0): "))
    longitud_deseada = float(input("Longitud deseada del pelo en centímetros (0.0): "))

    if longitud_inicial >= longitud_deseada:
        print("La longitud inicial no puede ser mayor o igual a la longitud deseada\n")
        return

    if longitud_inicial <= 0 or longitud_deseada <= 0:
        print("Las longitudes no pueden ser negativas o cero\n")
        return

    longitud = longitud_deseada - longitud_inicial

    print("Seleccione la unidad de tiempo deseada para la respuesta:")
    print("1. Días")
    print("2. Semanas")
    print("3. Meses")
    print("4. Años")
    unidad_tiempo = int(input("Opción (1 a 4): "))

    if unidad_tiempo > 4 or unidad_tiempo < 1:
        print("Opción inválida\n")
        return

    tiempo_crecimiento_meses = formula_velocidad('t', distancia=longitud, velocidad=TASA_CRECIMIENTO_PELO_CM_POR_MES)
    tiempo_crecimiento_meses = round(tiempo_crecimiento_meses, 4)

    tiempo_creimiento = 0
    unidad = "meses"

    match unidad_tiempo:
        case 1:
            tiempo_creimiento = meses_a_dias(tiempo_crecimiento_meses)
            unidad = "días"
        case 2:
            tiempo_creimiento = meses_a_semanas(tiempo_crecimiento_meses)
            unidad = "semanas"
        case 3:
            tiempo_creimiento = tiempo_crecimiento_meses
        case 4:
            tiempo_creimiento = meses_a_anios(tiempo_crecimiento_meses)
            unidad = "años"

    print(f"\nEl tiempo que tardará hasta la longitud deseada es de apróximadamente {tiempo_creimiento} {unidad}.")


TASA_CRECIMIENTO_PELO_CM_POR_MES = 2

if __name__ == "__main__":
    main()
