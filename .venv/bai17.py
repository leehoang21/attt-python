# Câu 17. Viết chương trình tìm số nguyên dương x
# nhỏ nhất sao cho giá trị của biểu thức Ax^2+Bx+C
# là một số nguyên tố với A,B,C là các số nguyên nhập vào từ bàn phím.
import math


def ptBac2(a: int, b: int, c: int):
    x = 0
    while x:
        x = a*x**2 + b*x + c
        expression += 1


print(ptBac2(1, 2, 1))
