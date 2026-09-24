"""SAHAKORN"""
import math as m
mem = input()
many = int(input())
tot = 0
dis = 1
for dis in range(many) :
    tot += float(input())
if mem == "Y" :
    dis = 0.95
elif mem == "N" and tot >= 500 :
    dis = 0.97
print(f"{m.ceil(tot * dis * 100) / 100:.2f}")
