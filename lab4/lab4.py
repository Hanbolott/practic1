def zadach1():
    try :
        a = int(input('Чтобы проверить деление на 3 ,введите число : '))
        b = a % 3
    except ValueError:
        print('Введено число !')
    else :
        if b == 0 and a !=0:
            print('Число', a , 'делятся на 3!')
        elif a ==0 :
            print('Введен ноль!')
        else:
            print('Число', a , 'не делятся на 3!')


def zadach2():
    try :
        a = int(input('Введите число - '))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен ноль')
    except ValueError:
        print('Введено не число')
    else :
        print('Результат деление 100 на введенное число:' , b )


def zadach3():
    data = input('Введите дату в формате дд.мм.гггг: ')
    data = data.split('.')
    if int(data[0])*int(data[1]) == int(data[2][2:4]):
        print('Ваша  дата рождения  магическая! :)')
    else:
        print('К сожелению у вас обычная дата рождение :( ')


def zadach4():
    a = int(input())
    sum_left = 0
    sum_right = 0
    for i in range(6):
        if i < 3:
            sum_right += a // 10 ** i % 10
        else:
            sum_left += a // 10 ** i % 10
    if sum_left == sum_right:
        print('Счастливый билет')
    else:
        print('Не счастливый билет')

zadach1()
zadach2()
zadach3()
zadach4()
