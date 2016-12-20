data = [{"electorate": 3100, "Money": 1050000},
        {"electorate": 2600, "Money": 750000},
        {"electorate": 3500, "Money": 1200000},
        {"electorate": 2800, "Money": 900000},
        {"electorate": 2400, "Money": 600000}]


res = []
def find_max(x,cash = 3000000):
    max = 0
    voice = 0
    money = 0

    for i in x:
        if cash - i["Money"] < 0:
            return res
    else:
        for i in x:
            if cash - i["Money"] > max:
                max = cash - i["Money"]
                voice = i["electorate"]
                money = i["Money"]
        ch = {"electorate": voice, "Money": money}
        res.append(ch)
        #print(res)
        data.remove(ch)
        #print("data", data)
        find_max(data, cash=max)

if __name__ == '__main__':
    find_max(data)
    print(res)


