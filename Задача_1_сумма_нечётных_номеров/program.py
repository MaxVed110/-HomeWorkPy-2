# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4


def SumOfOddPositions(list):
    sum = 0
    for i in range(0, list.__len__(), 2):
        sum += list[i]
    return sum


listUser = [1, 2, 3, 4, 5]
sumUser = SumOfOddPositions(listUser)
print(f"Сумма чисел списка, стоящих на нечетной позиции, равна: {sumUser}")
