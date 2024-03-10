def resolver_ecuacion_primero_grado(a, b):
    if a == 0:
        if b == 0:
            return "La ecuación es una identidad, tiene infinitas soluciones."
        else:
            return "La ecuación no tiene solución."
    else:
        x = -b / a
        return f"La solución de la ecuación es x = {x}"


def main():
    print("Calculadora de ecuaciones de primer grado (ax + b = 0)")
    try:
        a = float(input("Ingrese el coeficiente 'a': "))
        b = float(input("Ingrese el coeficiente 'b': "))
        solucion = resolver_ecuacion_primero_grado(a, b)
        print(solucion)
    except ValueError:
        print("Error: Por favor, ingrese coeficientes válidos (números).")


if __name__ == "__main__":
    main()