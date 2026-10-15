"""hod"""
inp = 0
data = []
res = []
first = 1
last = 1
while inp != -1 :
    inp = int(input())
    data.append(inp)
LONG = len(data)
for i in range(LONG) :
    if not i :
        first = data[i]
        last = data[i]
    elif (data[i] - data[i - 1]) == 1 :
        last = data[i]
    else :
        if first != last :
            res.append(f"{first}-{last}")
        else :
            res.append(data[i - 1])
        first = data[i]
        last = first
print(*res, sep=", ")
