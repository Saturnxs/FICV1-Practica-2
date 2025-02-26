def formula_velocidad(variable_retorno='v', distancia=0, tiempo=0, velocidad=0):
    match variable_retorno:
        case 'v':
            return distancia / tiempo
        case 'd':
            return velocidad * tiempo
        case 't':
            return distancia / velocidad


def formula_distancia(variable_retorno='d', velocidad_inicial=0, tiempo=1, aceleracion=0, distancia=0):
    match variable_retorno:
        case 'd':
            return velocidad_inicial * tiempo + (0.5 * aceleracion * tiempo**2)
        case 'vi':
            return (distancia - (0.5 * aceleracion * tiempo**2)) / tiempo
        case 'a':
            return (2 * (distancia - velocidad_inicial * tiempo)) / (tiempo**2)


def formula_velocidad_final(variable_retorno='vf', velocidad_inicial=0, aceleracion=0, tiempo=1, velocidad_final=0):
    match variable_retorno:
        case 'vf':
            return velocidad_inicial + aceleracion * tiempo
        case 'a':
            return (velocidad_final - velocidad_inicial) / tiempo
        case 't':
            return (velocidad_final - velocidad_inicial) / aceleracion
        case 'vi':
            return velocidad_final - aceleracion * tiempo
