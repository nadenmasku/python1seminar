number = input('Введите номер билета: ')
if len(number)==6:
    sum1 = int(number[0])+int(number[1])+int(number[2])
    sum2 = int(number[3])+int(number[4])+int(number[5])
    if sum1 == sum2: 
        print('Билет счастливый')
    else:
        print('Билет не счастливый')
else:
    print("Число не шестизначное")
