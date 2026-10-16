"""GABUANG"""
piece = 0
spot = 0
row = []
colpiece = []
colspot = []
size,cost = map(int,input().split())
for _ in range(size) :
    colpiece.append(0)#เก็บข้อมูลแถว
    colspot.append(0)
for _ in range(size) : #ขนาด
    row = list(map(int,input().split()))#input
    for i in range(size) :#เช็คแผ่น+รวมจุด
        if row[i] :
            piece += 1
            colpiece[i] = colpiece[i] + 1
        spot += row[i]
        colspot[i] += row[i]
    row.append(piece)
    row.append(spot)
    print(*row)#printแถว
    row = []
    piece = 0
    spot = 0
print(*colpiece)
print(*colspot)
print(sum(colpiece),sum(colspot),f"{sum(colspot) * cost:.2f}",sep=" ")
