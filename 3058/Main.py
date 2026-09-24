"""BRICKBRIDGE"""
import math as m
brk1 = int(input())
brk2 = int(input())
goal = int(input())
count = 0
if (brk2 * 5) + brk1 < goal :#กรณีอิฐไม่พอ
    count = -1
else :
    if goal - (brk2 * 5) <= 0 :#กรณีก้อนใหญ่อย่างเดียวก็เกิน/พอดี
        if goal % 5 :#ก้อนใหญ่ไม่เป๊ะ
            if brk1 >= goal % 5 :#ถ้าก้อนเล็กมีพอ
                count = goal % 5
            else :#ถ้าก้อนเล็กไม่พอ
                count = -1
    else :#ก้อนใหญ่อย่างเดียวไม่พอ
        if brk1 >= goal - (brk2 * 5) :#อิฐก้อนเล็กพอเติม
            count = m.ceil(goal - (brk2 * 5))
        else :#ก้อนเล็กไม่พอเติม
            count = -1
print(count)
