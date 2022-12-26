def pow(n: float, b: int):
    i = 0
    s = 1
    while i < b:
        i += 1
        s *= n
    return s


def decimalToFrac(n: float):
    i = 1
    while n % 1 != 0:
        n *= 10
        i *= 10
    j = 2
    while j <= n/2:
        while n % j == 0 and i % j == 0:
            n /= 2
            i /= 2
        j += 1
    return n//i, n % i, i


def root(a, n):
    r = 0
    pre = 1
    for item in range(5):
        while pow(r+pre, n) <= a:
            r += pre
        pre /= 10
    return r.__round__(5)


def powN(n: float, b: float):
    t = decimalToFrac(b)
    return pow(n, t[0]) * root(pow(n, t[1]), t[2])


print(powN(2, 2.56))
