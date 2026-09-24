"""POI"""
poi = int(input())
tot = 0
for i in range(poi) :
    plusminus = input()
    if plusminus == "+" :
        tot += 10
    if plusminus == "-" :
        tot -= 5
i = 0
print(tot + i)
