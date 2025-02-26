from utils.formulas import formula_velocidad
from utils.conversiones import centimetros_a_metros


def main():
    print("\nEste programa estima el tiempo que tarda un impulso nervioso en recorrer desde tu dedo del pie hasta la tu cabeza\n")

    altura_persona = float(input("Ingresa tu altura total en centímetros (0.0): "))
    altura_cabeza = float(input("Ingresa la altura de tu cabeza centímetros (0.0): "))

    if altura_cabeza > altura_persona:
        print("La altura de la cabeza no puede ser mayor a la altura total de la persona (osea what)\n")
        return

    if altura_cabeza <= 0 or altura_persona <= 0:
        print("Las alturas no pueden ser negativas o cero (osea what x2)\n")
        return

    distancia = altura_persona - altura_cabeza
    distancia = centimetros_a_metros(distancia)

    tiempo_impulso = formula_velocidad('t', distancia=distancia, velocidad=RAPIDEZ_IMPULSO_NERVIOSO_M_POR_S)
    tiempo_impulso = round(tiempo_impulso, 4)

    print(f"\nEl tiempo que tarda un impulso nervioso en recorrer desde el dedo del pie hasta la cabeza es de apróximadamente {tiempo_impulso} segundos.")


RAPIDEZ_IMPULSO_NERVIOSO_M_POR_S = 100

if __name__ == "__main__":
    main()
