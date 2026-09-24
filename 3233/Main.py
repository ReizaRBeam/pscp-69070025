"""LOTTERY"""
took = input().split()
buy = input().split()
let = took[0] == buy[0]
num = took[1] == buy[1]
las2 = took[1][3:5] == buy[1][3:5]
las3 = took[1][2:5] == buy[1][2:5]
if took == buy :
    print(1000000)
elif num :
    print(100000)
elif let and las3 :
    print(2000)
elif let and las2 :
    print(1000)
elif las3 :
    print(200)
elif las2 :
    print(100)
elif let :
    print(20)
else :
    print(0)
