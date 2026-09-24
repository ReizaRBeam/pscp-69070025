"""FROGJUMP"""
frog = input().split()
jump = int(frog[0])
far = int(frog[1])
total = 0
while jump > 0 and far > 0 :
    far -= jump
    jump -= 2
    total += 1
if far <= 0 :
    print(total)
elif jump <= 0 :
    print(-1)
