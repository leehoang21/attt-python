def decimalToBinary(a):
    list = []
    while a > 0:
        list.append(a % 2)
        a = a // 2
        print(a)
    return list


def nhapCoLap(a, k, n):
    listk = decimalToBinary(k)
    b = 1
    if k == 0:
        return b
    A = a
    if listk[0] == 1:
        b = a
    for i in range(1, len(listk)):
        A = (A*A) % n
        if listk[i] == 1:
            b = (b*A) % n

    return b


def febma(n, k):
    for item in range(k):
        a = 2+k
        if (a > n-2):
            return False
        r = nhapCoLap(a, n-1, n)
        if r != 1:
            return False

    return True
