# Câu 23. Viết chương trình in ra màn hình YES trong trường hợp
# tổng của các số nguyên tố trong khoảng [A, B] là cũng là một số
# nguyên tố và NO nếu ngược lại. Với A,B là hai số được nhập vào
# từ bàn phím.
def isPrime(n):
    if n < 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
    return True


def bai23(a, b):
    list = []
    for item in range(a, b+1):
        if isPrime(item):
            list.append(item)
    return list


print(bai23(0, 100))
