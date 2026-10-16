"""COOK"""
ingre = ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
         "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
ingre.sort()
tasty = ["Sweet","Sour","Salty"]
tasty.sort()
had = []
no = []
ew = []
inp = ""
ing = False
tas = False
while True :
    inp = input()
    if inp == "Cook" :
        break
    if inp in ingre and inp not in had :
        had.append(inp)
    elif inp not in ingre:
        no.append(inp)
had.sort()
if had == ingre :
    ing = True
had = []
while True :
    inp = input()
    if inp == "End" :
        break
    if inp in tasty and inp not in had :
        had.append(inp)
    elif inp not in tasty:
        ew.append(inp)
had.sort()
if had == tasty :
    tas = True

if no :
    print("This is not Pad Thai!!!")
elif not ing :
    print("This is bad!")
elif ing and (ew or not tas) :
    print("Not Bad...")
elif ing and tas :
    print("Delicious!")
