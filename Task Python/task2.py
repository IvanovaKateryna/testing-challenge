peoples = [raw_input('Write data in format "Name Surname Age Sex  ')
           for _ in range(int(raw_input("Write number of People:  ")))]


def peopleformat(func):
    def peopletoformat(peoples):
        for i in range(len(peoples)):
            temp = peoples[i].strip().split()
            if temp[-1] == 'M':
                flag = 'Mr. '
            else:
                flag = 'Ms. '
            peoples[i] = [flag + ' '.join(temp[:-2]), int(temp[-2])]
        return func(peoples)
    return peopletoformat


@peopleformat
def peoplesort(peoples):
    for x, y in sorted(peoples, key=lambda x: x[1]):
        print(x)


peoplesort(peoples)
