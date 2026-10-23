"""PAIR"""
inp = input()
data = []
rev = inp[::-1]
for i in rev :
    if i not in data :
        data.append(i)
    else :
        data.remove(i)
if not data :
    print("fully paired")
elif data :
    print(*data[::-1],sep="")
