import math

# Funciones básicas
def suma(a, b):
    return (a[0] + b[0], a[1] + b[1])

def resta(a, b):
    return (a[0] - b[0], a[1] - b[1])

def producto(a, b):
    real = a[0] * b[0] - a[1] * b[1]
    imag = a[0] * b[1] + a[1] * b[0]
    return (real, imag)

def division(a, b):
    divisor = b[0] ** 2 + b[1] ** 2
    if divisor == 0:
        raise ValueError("División por cero no permitida.")
    real = (a[0] * b[0] + a[1] * b[1]) / divisor
    imag = (a[1] * b[0] - a[0] * b[1]) / divisor
    return (real, imag)

def modulo(a):
    return math.sqrt(a[0] ** 2 + a[1] ** 2)

def conjugado(a):
    return (a[0], -a[1])

# Conversión
def polar_a_cartesiano(p):
    real = p[0] * math.cos(p[1])
    imag = p[0] * math.sin(p[1])
    return (real, imag)

def cartesiano_a_polar(a):
    magnitud = modulo(a)
    angulo = math.atan2(a[1], a[0])
    return (magnitud, angulo)

def fase(a):
    return math.atan2(a[1], a[0])
