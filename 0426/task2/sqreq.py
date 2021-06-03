def solveSquare(a, b, c):
    if (a ==0):
    	if (b == 0):
    		if (c ==0):
    			return "∞"
    		else:
    			return "∅"
    	else:
    		return str(-c/b)
    D = b**2 - 4 * a * c
    if D > 0:
        return str((-b - D**(0.5)) / (2 * a)) + " " + str((-b + D**(0.5)) / (2 * a))
    elif D < 0:
        return "∅"
    else:
        return str(-b / (2 * a))