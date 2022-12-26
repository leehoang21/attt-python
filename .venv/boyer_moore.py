def boyerMoore(str1: str, str2: str):
    i = str1.__len__()-1
    j = str2.__len__()-1
    while i > 0:
        if (str1[i] == str2[j]):
            print('3', i, j)
            i -= 1
            j -= 1
        else:
            i = jump(str1, str2, i, j)
            j = str2.__len__()-1
        #
        if j < 0:
            return i
    return -1


def jump(str1: str, str2: str, i, j):
    for item in range(str2.__len__()):
        if str1[i] == str2[item] and item < j:
            i = i+j-item+1
            print('1', i, j)
            break
    else:
        print('2', i, j)
        i += str2.__len__()
    return i


print(boyerMoore('str1', 'str'))
