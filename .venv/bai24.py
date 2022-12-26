# Câu 24. Đặt S1, S2 là các mảng chứa giá trị bình phương của các
# số nguyên. Hãy viết chương trình in ra số lượng tất cả các số
# nguyên tố nằm trong khoảng [a,b] sao cho số này cũng là tổng
# của hai số x và y với x thuộc S1 và y thuộc S2. Trong đó, a,b
# là các số được nhập từ bàn phím
# Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng
# [10,15] chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có
# 13 = 2^2 + 3^2=4+9.
# Gợi ý: Sử dụng hàm isPrime() đã được viết trong bài 23.
def isPrime(n):
    if n < 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
    return True


def bai24(a, b):
    list = []
    for item in range(a, b+1):
        if isPrime(item):
            r = int(root(item))+1
            for i in range(1, r):
                for j in range(i, r):
                    kq = i*i + j*j
                    if kq == item:
                        list.append(item)
                    if kq > item:
                        break
    return list


def root(a):
    r = 0
    pre = 0.001
    while r*r <= a:
        r += 1
    while r*r >= a:
        r -= pre
    return r+pre


print(bai24(1, 10000))
