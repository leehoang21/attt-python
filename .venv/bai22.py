# Câu 22. Với một số nguyên dương N thoả mãn 0<N<10000, đặt:
# F ( N ) = N nếu N là một số nguyên tố
# F ( N ) = 0 nếu là hợp số
# Cho  L và R nhập vào từ bàn phím, với mọi cặp i , j
# trong khoảng [ L , R ] hãy viết chương trình in ra màn hình
# giá trị của tổng F ( i ) * F ( j ) với  j > i.

def isPrime(n):
    if n < 4:
        return n > 1
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i <= n/2:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def cau22(l, r):
    count = 0
    for item in range(l, r+1):
        for item2 in range(item+1, r+1):
            if isPrime(item) and isPrime(item2):
                count += item * item2
    return count


print(isPrime(5))
print(cau22(2, 10))
