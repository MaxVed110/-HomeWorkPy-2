# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def ProductOfPairsOfNumbersInTheList(list):
    productNumbersList = []
    if(list.__len__() % 2 == 0):
        for i in range(int(list.__len__()/2)):
            productNumbersList.append(list[i]*list[list.__len__()-1-i])
    else:
        for i in range(int(list.__len__()/2)):
            productNumbersList.append(list[i]*list[list.__len__()-1-i])
        productNumbersList.append(list[int(list.__len__()/2)+1]**2)
    return productNumbersList


listUser = [2, 3, 4, 5, 6]
productUserList = ProductOfPairsOfNumbersInTheList(listUser)
print(f"Произведение пар чисел в списке равно: {productUserList}")
