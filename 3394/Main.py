"""SEND"""
tot,fst = map(int,input().split())
data = {}
cou = 0
que = 0
for i in range(tot) :
    data[i + 1] = int(input())
while True :
    print(data)
    i = 1
    if i == 1 :
        que = data.pop(fst)
        if not que :
            cou = 1
    elif que in data :
        que = data.pop(que)
        cou += 1
    elif que not in data :
        break
    i += 1
print(cou)
