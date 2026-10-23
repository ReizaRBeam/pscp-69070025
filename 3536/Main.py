"""PRIME"""
inp = int(input())
prime = True
root = int(inp ** 0.5)
if inp == 2 :
    prime = True
elif inp <= 1 or not inp % 2:
    prime = False
else:
    for i in range(3, root + 1, 2):
        if not inp % i :
            prime = False
            break

if prime:
    print("YES")
else:
    print("NO")
