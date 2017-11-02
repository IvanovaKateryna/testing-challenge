peoples = [input('Введите данные в формате "Имя Фамилия Возраст Пол"')
           for _ in range(int(input("Введите количество людей")))]


def peopleformat(func):
    def peopletoformat(peoples):
        for i in range(len(peoples)):
            temp = peoples[i].strip().split()
            if temp[-1] == 'М':
                flag = 'Г-н. '
            else:
                flag = 'Г-жа '
            peoples[i] = [flag + ' '.join(temp[:-2]), int(temp[-2])]
        return func(peoples)
    return peopletoformat


@peopleformat
def peoplesort(peoples):
    for x, y in sorted(peoples, key=lambda x: x[1]):
        print(x)


peoplesort(peoples) 
