xline = [input('Строка Х   ')for _ in range(int(input('Введите количество элементов Х  ')))]
yline = [input('Строка Y   ')for _ in range(int(input('Введите количество элементов Y  ')))]


def numberyinx():
    for i in yline:
        sum = 0
        for j in xline:
            if i == j:
                sum += 1
        print('Количество элемента ', i, 'в массиве Х = ', sum)


numberyinx()
