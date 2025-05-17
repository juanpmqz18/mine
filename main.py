# main.py
from calculadora import *
import math

def mostrar_menu():
    print("\n--- Calculadora Científica ---")
    print("1. Sumar (a + b)")
    print("2. Restar (a - b)")
    print("3. Dividir (a / b)")
    print("4. Seno")
    print("5. Coseno")
    print("6. Tangente")
    print("7. Inverso de Seno (arcsin)")
    print("8. Inverso de Coseno (arccos)")
    print("9. Inverso de Tangente (arctan)")
    print("10. x elevado a la y (x^y)")
    print("11. Logaritmo base 10")
    print("12. Logaritmo Natural")
    print("13. Raíz Cuadrada")
    print("14. Raíz Enésima")
    print("15. Factorial")
    print("16. Inverso (1/x)")
    print("17. Valor de Pi")
    print("18. Seno Hiperbólico")
    print("19. Coseno Hiperbólico")
    print("20. Tangente Hiperbólica")
    print("21. Combinatoria (n C r)")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                a = float(input("a: "))
                b = float(input("b: "))
                print("Resultado:", sumar(a, b))

            elif opcion == "2":
                a = float(input("a: "))
                b = float(input("b: "))
                print("Resultado:", restar(a, b))

            elif opcion == "3":
                a = float(input("Dividendo: "))
                b = float(input("Divisor: "))
                print("Resultado:", dividir(a, b))

            elif opcion == "4":
                x = float(input("Ángulo en radianes: "))
                print("Resultado:", seno(x))

            elif opcion == "5":
                x = float(input("Ángulo en radianes: "))
                print("Resultado:", coseno(x))

            elif opcion == "6":
                x = float(input("Ángulo en radianes: "))
                print("Resultado:", tangente(x))

            elif opcion == "7":
                x = float(input("Valor entre -1 y 1: "))
                print("Resultado:", arcseno(x))

            elif opcion == "8":
                x = float(input("Valor entre -1 y 1: "))
                print("Resultado:", arccoseno(x))

            elif opcion == "9":
                x = float(input("Número real: "))
                print("Resultado:", arctangente(x))

            elif opcion == "10":
                x = float(input("Base (x): "))
                y = float(input("Exponente (y): "))
                print("Resultado:", potencia(x, y))

            elif opcion == "11":
                x = float(input("Número positivo: "))
                print("Resultado:", log_base_10(x))

            elif opcion == "12":
                x = float(input("Número positivo: "))
                print("Resultado:", log_natural(x))

            elif opcion == "13":
                x = float(input("Número positivo: "))
                print("Resultado:", raiz_cuadrada(x))

            elif opcion == "14":
                x = float(input("Número: "))
                n = float(input("Índice (n): "))
                print("Resultado:", raiz_enesima(x, n))

            elif opcion == "15":
                x = int(input("Número entero no negativo: "))
                print("Resultado:", factorial(x))

            elif opcion == "16":
                x = float(input("Número distinto de 0: "))
                print("Resultado:", inverso(x))

            elif opcion == "17":
                print("Resultado:", pi())

            elif opcion == "18":
                x = float(input("Número: "))
                print("Resultado:", seno_hiperbolico(x))

            elif opcion == "19":
                x = float(input("Número: "))
                print("Resultado:", coseno_hiperbolico(x))

            elif opcion == "20":
                x = float(input("Número: "))
                print("Resultado:", tangente_hiperbolica(x))

            elif opcion == "21":
                n = int(input("n: "))
                r = int(input("r: "))
                print("Resultado:", combinatoria(n, r))

            elif opcion == "0":
                print("Saliendo...")
                break

            else:
                print("❌ Opción no válida. Intenta de nuevo.")

        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()
