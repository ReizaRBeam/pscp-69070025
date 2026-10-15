"""GIRAFFE"""
allg = int(input())
summ = 0
stat = [0,0]
for i in range(allg + 1) :
    if not i == allg :
        stat.insert(i + 1,int(input()))
    fst = not i - 1 and stat[i - 1] > stat[i]
    lst = i == allg and stat[i + 1] > stat[i]
    mid = bool(stat[i] > stat[i - 1] and stat[i] > stat[i + 1] and allg)
    if fst or lst :
        summ += 1
    if mid :
        summ += 1
print(summ)
