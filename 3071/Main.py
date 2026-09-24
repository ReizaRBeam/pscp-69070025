"""หารเหลือเศษ"""
num1 = int(input())
num2 = int(input())
han = int(input())
ses = int(input())
count = 0
for i in range(num2 - num1 + 1) :
    if (num1 + i) % han == ses :
        count += 1
print(count)
