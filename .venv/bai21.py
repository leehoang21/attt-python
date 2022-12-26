# Câu 21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố
# từ 1 đến X (ngoại trừ X) là một số nguyên tố. Hãy viết chương trình
#  đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước
#  nhập từ bàn phím.
def isPrime(n):
    if n < 4:
        return n > 1
    if (n % 2 == 0 or n % 3 == 2):
        return False
    i = 5
    while i+2 < n/2:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def isSuperPrime(a):
    count = 0
    for i in range(1, a):
        if isPrime(i):
            count += 1
    return isPrime(count)


def cau21(a, b):
    count = 0
    list = []
    for i in range(a, b+1):
        if isSuperPrime(i):
            count += 1
            list.append(i)
    return list


print(cau21(1, 100))
