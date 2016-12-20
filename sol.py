#ТАБЛИЦА ИЗ УСЛОВИЯ ЗАДАЧИ
data = [{"electorate": 3100, "Money": 1050000},
        {"electorate": 2600, "Money": 750000},
        {"electorate": 3500, "Money": 1200000},
        {"electorate": 2800, "Money": 900000},
        {"electorate": 2400, "Money": 600000}]

#МЕТОД НАХОЖДЕНИЯ МИНИМАЛЬНОЙ СУММЫ НАШИХ ДАННЫХ
def my_min(arr):
    min = data[0]['Money']
    for i in arr:
        if min > i['Money']:
            min = i['Money']
    return min

#МЕТОД НАХОЖДЕНИЯ МАКСИМАЛЬНОГО КОЛИЧЕСТВА ГОЛОСОВ ИЗ НАШИХ ДАННЫХ
def max_v(arr):
    max = 0
    for i in arr:
        if max < i['electorate']:
            max = i['electorate']
            el = i
    return el


res = []

#ОСНОВНОЙ МЕТОД, НАХОДЯЩИЙ ОПТИМАЛЬНОЕ ПО ЦЕНЕ РЕШЕНИЕ.
#РЕАЛИЗОВАН В ВИДЕ РЕКУРСИИ
def find_max(x,cash = 3000000):
    max = 0
    for i in x:
        if cash - i["Money"] < 0:
            return res

    for i in x:
        if cash - i["Money"] > max:
            max = cash - i["Money"]
            if cash - i["Money"] > my_min(data):
                ch = i
            else:
                ch = max_v(data)
    res.append(ch)
    data.remove(ch)
    find_max(data, cash=max)

if __name__ == '__main__':
    find_max(data)
    print(res)



