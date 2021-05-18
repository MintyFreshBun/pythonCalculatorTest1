import calculator1 as calc

def tabuada(nr):
    c = calc.Calculator()
    tab = []
    for i in range(1, 11):
        res, s1 = c.mul(nr, i)
        tab.append(s1)
    return tab