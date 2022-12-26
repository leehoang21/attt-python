# Câu 18. Áp dụng thuật toán đã được học để viết chương trình
# tính tổng của hai số nguyên lớn, hiển thị dưới mạng mảng và
# dạng số nguyên.
import math


def bieuDienSoDangMang(soBit, so, heSo):
    sodangMang = []
    leghtSoDangMang = math.log2(heSo) // soBit
    for i in range(int(leghtSoDangMang), -1, -1):
        x = math.pow(2, soBit*i)
        sodangMang.append(so // x)
        so = so % x
    return sodangMang


def mangSangSo(soBit, soDangMang):
    so = 0
    for i in range(len(soDangMang)):
        so += soDangMang[i] * math.pow(2, soBit*(len(soDangMang)-i-1))
    return so


def plusNumberTypeList(a, b):
    tong = []
    for i in range(0, len(a) if len(a) > len(b) else len(b)):
        if (i >= len(a)):
            tong.append(b[i])
        elif (i >= len(b)):
            tong.append(a[i])
        else:
            tong.append(a[i] + b[i])
    return tong


print(mangSangSo(8, plusNumberTypeList(
    [0, 11, 173, 248], [0, 1, 226, 64, 55])))
print(mangSangSo(8, [0, 11, 173, 248])+mangSangSo(8, [0, 1, 226, 64, 55]))
