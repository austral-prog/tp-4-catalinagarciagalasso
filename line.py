def line():
    coeficiente_A = float(input("Ingrese coeficiente A: "))
    coeficiente_B = float(input("Ingrese coeficiente B: "))
    coeficiente_X1 = float(input("Ingrese coeficiente X1:"))
    coeficiente_X2 = float(input("Ingrese coeficiente X2:"))
    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_X2}")

    print("\nPara la siguiente ecuación:")
    print(f"\tY = {coeficiente_A}X + {coeficiente_B}")

    print("\nDados los siguientes puntos:")
    P1 = (50.0, 110.99999999999999)
    P2 = (-32.9, -79.66999999999999)
    print(f"\tP1 {P1}")
    print(f"\tP2 {P2}")
    y2 = -79.66999999999999
    y1 = 110.99999999999999
    x2 = -32.9
    x1 = 50.0
    distancia = float(((y2 - y1)**2 + (x2 - x1)**2)**0.5)
    print(f"\nLa distancia entre ellos es: {distancia}")
