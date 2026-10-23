"""AMOGUS"""
import json
peo = {}
dead = {}
getallname = False
while True :
    inp = input()
    if not getallname :
        if inp == "Start" :
            getallname = True
        else :
            peo.update(json.loads(inp))

    if getallname and inp != "Start" :
        if inp == "End" :
            break
        dead[inp] = peo.pop(inp)

sorted_alive = dict(sorted(peo.items()))
sorted_dead = dict(sorted(dead.items()))

imp = sum(1 for value in sorted_alive.values() if value == "Impostor")

print(f"{imp} Impostor Remains")
print("***Alive***")
for key, value in sorted_alive.items():
    print(f"{key} : {value}")
print("***Dead***")
for key, value in sorted_dead.items():
    print(f"{key} : {value}")
