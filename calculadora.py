# calculadora.py
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arcseno(x):
    return math.asin(x)

def arccoseno(x):
    return math.acos(x)

def arctangente(x):
    return math.atan(x)

def potencia(x, y):
    return math.pow(x, y)

def log_base_10(x):
    return math.log10(x)

def log_natural(x):
    return math.log(x)

def raiz_cuadrada(x):
    return math.sqrt(x)

def raiz_enesima(x, n):
    return x ** (1/n)

def factorial(x):
    if x < 0:
        raise ValueError("El factorial no está definido para números negativos")
    return math.factorial(x)

def inverso(x):
    if x == 0:
        raise ValueError("No se puede dividir entre cero")
    return 1 / x

def pi():
    return math.pi

def seno_hiperbolico(x):
    return math.sinh(x)

def coseno_hiperbolico(x):
    return math.cosh(x)

def tangente_hiperbolica(x):
    return math.tanh(x)

def combinatoria(n, r):
    return math.comb(n, r)
