"""AEIOU"""
inp = input()
a = 0
e = 0
i = 0
o = 0
u = 0
for j in inp :
    if j in ("A","a") :
        a += 1
    elif j in ("E","e") :
        e += 1
    elif j in ("I","i") :
        i += 1
    elif j in ("O","o") :
        o += 1
    elif j in ("U","u") :
        u += 1
if a > 0 :
    print(f"a : {a}")
if e > 0 :
    print(f"e : {e}")
if i > 0 :
    print(f"i : {i}")
if o > 0 :
    print(f"o : {o}")
if u > 0 :
    print(f"u : {u}")
