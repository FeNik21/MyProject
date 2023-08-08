a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print('1. +, 2. - 3. *, 4. /, 5. степень, 6. деление без остатка, 7. выключить калькулятор')
c = int(input('Введите число соответствующее действию: '))

def calc(a, b, c):
        try:
            if c == 1:
                a += b
            elif c == 2:
                a -= b
            elif c == 3:
                a *= b
            elif c == 4:
                a /= b
            elif c == 5:
                a **= b
            elif c == 6:
                a //= b
            else:
                print('Результат не возможен')
        except ZeroDivisionError:
            print('На 0 делить нельзя')
        return a

calc(a, b, c)
d = calc(a, b, c)
print('Result: ', d)