# Câu 26. Một số được gọi là số mạnh mẽ khi nó đồng thời vừa
# chia hết cho số nguyên tố và chia hết cho bình phương của số
# nguyên tố đó. Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000).
def isPrime(n):
    if n < 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            print(item)
            return False
    return True


def bai26(a):
    i = 2
    while i*i <= a/2:
        if isPrime(item) and a % (item ** 2) == 0:
            print(item)
