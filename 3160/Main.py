"""PRIME"""
num = input().split()
tot = []
summ = 0
prime = True
for i in range(int(num[0]),int(num[1]) + 1) :
    if i > 1 :
        for j in range(2,i) :
            prime = i % j
            if not prime :
                break
    if prime and i > 1 :
        tot.append(i)
        summ += 1
    prime = True
if len(tot) >= 1 :
    X = " ".join(map(str, tot))
    print(X)
print(f"Total primes: {summ}")
