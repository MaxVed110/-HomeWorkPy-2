# Написать программу преобразования десятичного числа в двоичное

def DecimalInBinary(numberDecimal):
    numberBinary = 0
    count = 0
    while(numberDecimal > 0):
        numberBinary += numberDecimal % 2*10**count
        numberDecimal = int(numberDecimal / 2)
        count += 1
    return numberBinary


numberUser = 10
numberBinary = DecimalInBinary(numberUser)
print(f"Число {numberUser} в двоичной системе равно: {numberBinary}")
