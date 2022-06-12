# Programa raiz quadrada
def jsqrt(sqrvar1):
    sqrvar2 = sqrvar1
    for sqrvar3 in range(0, 11):
        sqrvar4 = -((sqrvar1 - sqrvar2 ** 2) / (2 * sqrvar2))
        sqrvar2 = sqrvar2 - sqrvar4
    return sqrvar2


def eqs(sga, sgb, sgc):
    delta = (sgb ** 2) - (4 * sga * sgc)
    x1 = 0
    x2 = 0
    if delta > 0:
        x1 = (-sgb + (jsqrt(delta)) / 2 * sga)  # type: float
        x2 = (-sgb - (jsqrt(delta)) / 2 * sga)  # type: float
    return (x1, x2)


def jcubrt(cubvar1):
    cubvar2 = jsqrt(cubvar1)
    for cubrange in range(0, 11):
        print(cubvar2)
        if (cubvar2**3) > cubvar1:
            cubresult = eqs(cubvar2*3, (cubvar2**2)*-3, cubvar2**3-cubvar1)
            if cubresult[0] > cubresult[1]:
                cubvar2 = float(cubvar2-cubresult[0])
            elif cubresult[0] < cubresult[1]:
                cubvar2 = float(cubvar2 - cubresult[1])
        elif (cubvar2**3) < cubvar1:
            cubresult = eqs(cubvar2*3, (cubvar2**2)*3, cubvar2**3-cubvar1)
            if cubresult[0] > cubresult[1]:
                cubvar2 = float(cubvar2 + cubresult[0])
            elif cubresult[0] < cubresult[1]:
                cubvar2 = float(cubvar2 + cubresult[1])
    return (cubvar2)

print(jcubrt(9))