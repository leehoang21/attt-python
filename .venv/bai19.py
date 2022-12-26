# Câu 19. Viết chương trình in ra các số nguyên dương nằm trong
# khoảng [m,l] sao cho giá trị của biểu thức Ax^2+Bx+C là một số
# nguyên tố. Với A,B,C, m,l là các số nguyên nhập từ bàn phím
# (m<l).
def isPrime(n):
    if n < 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
    return True


def bai19(m, l, a, b, c):
    for item in range(m, l+1):
        if isPrime(a*item*item+b*item+c):
            print(item)


bai19(1, 10, 2, 3, 4)
