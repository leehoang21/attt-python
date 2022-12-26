# Câu 27. Viết chương trình in ra các cặp số (a,b) thoả mãn điều
# kiện 0<a,b<1000, sao cho ước chung lớn nhất của 2 số đó là một
# số nguyên tố.
def UCLN(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp

    return a


def isPrime(n):
    if n < 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
    return True


def bai27():
    for a in range(1, 100):
        for b in range(a+1, 100):
            if isPrime(UCLN(a, b)):
                print(a, b, UCLN(a, b))


bai27()
