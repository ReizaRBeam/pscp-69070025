"""HUATAW"""
way = input()
weight = float(input())
rate = {"BKK CNX" : (10,30),
        "CNX UBP" : (15,40),
        "UBP BKK" : (20,40),
        "BKK PKT" : (25,50),
        "PKT CNX" : (30,60),
        "UBP PKT" : (40,70)}

if way not in rate :
    print("Error")
else :
    print(f"{rate[way][0] + (rate[way][1] * weight):.2f}")
