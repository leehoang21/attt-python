# Câu 20. Viết chương trình in ra các cặp số (A,B) nằm
# trong khoảng (M,N) sao cho ước số chung lớn nhất của A và
# B có giá trị là một số D cho trước. Với M,N,D nhập vào từ
# bàn phím. (0<M,N, D < 1000).
def uocSoChungLonNhat(a, b):
    if a == 0 or b == 0:
        return a+b
    return uocSoChungLonNhat(b, a % b)


def inCacCapSo():
    m = int(input("Nhập vào số M: "))
    n = int(input("Nhập vào số N: "))
    d = int(input("Nhập vào số D: "))
    start = 0
    if d < 0 or n < 0 or m < 0 or m > n or d > n:
        print("Invalid input")
        return
    x = 0
    while true:
        if d*x < n and d*x > m:
            start = d*x
            break
    for i in range(start, n, d):
        for j in range(i+d, n, d):
            if uocSoChungLonNhat(i, j) == d:
                print(f"({i}, {j})")


inCacCapSo()
