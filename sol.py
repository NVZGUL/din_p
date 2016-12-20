data = [{"electorate": 3100, "Money": 1050000},
        {"electorate": 2600, "Money": 750000},
        {"electorate": 3500, "Money": 1200000},
        {"electorate": 2800, "Money": 900000},
        {"electorate": 2400, "Money": 600000}]


def find_voice_cost(arr):
    c_arr = []
    for i in arr:
        c_arr.append(i['Money']/i['electorate'])
    return c_arr

def my_min(val,arr):
    for i in arr:
        if val <= i:
            return True
        else:
            return False
res = []
cheep_v = find_voice_cost(data)
def find_max(x,cash = 3000000):
    max = 0
    min = 0
    voice = 0
    money = 0
    for i in x:
        if cash - i["Money"] < 0:
            return res
    else:
        for i in x:
            if cash - i["Money"] > max and my_min(i["Money"]/i["electorate"], cheep_v):
                max = cash - i["Money"]
                voice = i["electorate"]
                money = i["Money"]
                ch1 = i["Money"]/i["electorate"]
        ch = {"electorate": voice, "Money": money}
        res.append(ch)
        #print(res)
        data.remove(ch)
        cheep_v.remove(ch1)
        #print(cheep_v)
        find_max(data, cash=max)

if __name__ == '__main__':
    find_max(data)
    print(res)



