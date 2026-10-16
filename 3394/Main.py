"""SEND"""
tot,fst = map(int,input().split())
data = {}
cou = 0
que = 0
for i in range(tot) :
    data[i + 1] = int(input())
num = 1
while True :
    if num == 1 :
        que = data.pop(fst, "Not Found")
        cou += 1
    elif que in data :
        que = data.pop(que, "Not Found")
        cou += 1
    elif que not in data or que == "Not Found" :
        break
    num += 1
print(cou)
