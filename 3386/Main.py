"""DUP"""
m = int(input())
n = int(input())
mstat = []
dupl = []
dup = False
for i in range(m + n) :
    cod = input()
    if i + 1 <= m :
        mstat.append(cod)
    else :
        if cod in mstat :
            dup = True
            dupl.append(cod)
if dup :
    dupl.sort(reverse=True)
    print(*dupl,sep="\n")
elif not dup :
    print("Nope")
