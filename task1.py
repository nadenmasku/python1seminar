number = input("Введите трехзначное число: ")

if len(str(number))  == 3:
    sum = int(number[0])+int(number[1])+int(number[2])
    print(sum)
else:
    print('Число не трёхзначное')