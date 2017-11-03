xline = [raw_input('Line x   ')for _ in range(int(raw_input('Write number of x  ')))]
yline = [raw_input('Line y   ')for _ in range(int(raw_input('Write number of y  ')))]


def numberyinx():
    for i in yline:
        sum = 0
        for j in xline:
            if i == j:
                sum += 1
        print('Number of element ', i, 'in x = ', sum)


numberyinx()
