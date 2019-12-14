a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

if a > b and a > c:
    print ('Максимальное число:', a )
elif b > a and b > c:
    print ('Максимальное сисло:', b)
else:
    print ('Максимальное число:', c)
    