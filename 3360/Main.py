"""PANG"""
w,h,m,n = map(int,input().split())
knifex = list(map(int,input().split()))
knifey = list(map(int,input().split()))
x,y = 0,0
piece = []
for i in range(m + 1) :
    if not i :
        x = knifex[0]
    elif i == len(knifex) :
        x = w - knifex[i - 1]
    else :
        x = knifex[i] - knifex[i - 1]
    for j in range(n + 1) :
        if not j :
            y = knifey[0]
        elif j == len(knifey) :
            y = h - knifey[j - 1]
        else :
            y = knifey[j] - knifey[j - 1]
        piece.append(x * y)
piece.sort()
print(f"{piece[-1]} {piece[-2]}")
