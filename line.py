def line():
    coeficiente_A = float(input("Ingrese coeficiente A: "))
    coeficiente_B = float(input("Ingrese coeficiente B: "))
    coeficiente_X1 = float(input("Ingrese coeficiente X1:"))
    coeficiente_X2 = float(input("Ingrese coeficiente X2:"))
    coeficiente_Y1 = (coeficiente_A * coeficiente_X1 + coeficiente_B)
    coeficiente_Y2 = (coeficiente_A * coeficiente_X2 + coeficiente_B)
    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_X2}")

    print("\nPara la siguiente ecuación:")
    print(f"\tY = {coeficiente_A}X + {coeficiente_B}")

    print("\nDados los siguientes puntos:")
    p = [coeficiente_X1, coeficiente_Y1]
    q = [coeficiente_X2, coeficiente_Y2]

    P1_str = f"P1 ({coeficiente_X1}, {coeficiente_Y1})"
    P2_str = f"P2 ({coeficiente_X2}, {coeficiente_Y2})"
    print(f"\t{P1_str}")
    print(f"\t{P2_str}")
    distancia = float(((coeficiente_Y2 - coeficiente_Y1)**2 + (coeficiente_X2 - coeficiente_X1)**2)**0.5)
    print(f"\nLa distancia entre ellos es: {distancia}")
