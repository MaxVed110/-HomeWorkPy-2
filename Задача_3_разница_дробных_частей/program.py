# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def DifferenceMaxMin(list):
    difference = 0
    listBuf = []
    for i in range(list.__len__()):
        if(type(list[i]) == float):
            listBuf.append(list[i] % 1)
    difference = round(max(listBuf), 2) - round(min(listBuf), 2)
    return difference


listUser = [1.1, 1.2, 3.1, 5, 10.01]
differenceUser = DifferenceMaxMin(listUser)

print(f"Разница между максимальным и минимальным значением дробной части элементов равна: {differenceUser}")
