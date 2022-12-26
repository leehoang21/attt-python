def UCLN(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp

    return a


def BCNN(a, b):
    return a*b//UCLN(a, b)


print(UCLN(4, 8))
