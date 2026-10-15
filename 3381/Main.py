"""DOTDOTDOT"""
data = []
long = 0
test = int(input())
for _ in range(test) :
    many = int(input())
    for _ in range(many) :
        x,y = list(map(int,input().split()))
        f = x + y
        data.append((x,y,f))
    data.sort(key=lambda x: (x[2],x[0]))
    long = len(data)
    for i in range(long) :
        print(f"{data[i][0]} {data[i][1]}")
    data = []
