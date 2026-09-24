"""Storechck"""
inp = input().split()
tim = ()
ope = {}
op = []
yes = 0
for i in range(int(inp[0])) :
    time = input().split()
    tim = (int(time[0]),int(time[1]))
    ope[i] = tim
check = input().split()
for i in range(int(inp[1])) :
    for j in range(int(inp[0])) :
        if ope[j][0] <= int(check[i]) < ope[j][1] :
            yes += 1
    op.append(yes)
    yes = 0
    print(op[i],end=" ")
