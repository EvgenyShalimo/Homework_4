import datetime
import time


n = int(input('Введите количество элементов списка:'))
t = datetime.datetime.today()


def vremya(x):
    lest_1 = []
    for i in range(x):
        t = datetime.datetime.today()
        t_1 = t.strftime('%Y-%m-%d %H:%M:%S')
        lest_1.append(t_1)
        print('Текущее время:', t_1)
        time.sleep(1)
    else:
        return print(lest_1)
        yield


a = vremya(n)
for u in a:
    print(u)
print(type(a))
