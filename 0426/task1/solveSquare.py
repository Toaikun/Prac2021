def solveSquare(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        return ((-b - D**(0.5)) / (2 * a), (-b + D**(0.5)) / (2 * a))
    elif D < 0:
        return None
    else:
        return (-b / (2 * a), -b / (2 * a))