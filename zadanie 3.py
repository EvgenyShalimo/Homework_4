numb = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 1]
numb_2 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, ]


def numb_1(x):
    numb_dict = {}
    for i in x:
        if numb_dict.get(i, None):
            numb_dict[i] += 1
        else:
            numb_dict[i] = 1
    return numb_dict


print(numb_1(numb))
print(numb_1(numb_2))
