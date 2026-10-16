"""CATFOX"""
import json
import re

data = {}
roun = int(input())
for _ in range(roun):
    data.update(json.loads(input()))

if "Garfield" not in data and "Cat01" not in data.values():
    data["Garfield"] = "Cat01"
if "Fubuki" not in data and "Fox01" not in data.values():
    data["Fubuki"] = "Fox01"

sorted_data = dict(
    sorted(
        data.items(),
        key=lambda item: (
            re.match(r"([a-zA-Z]+)(\d+)", item[1]).group(1),
            int(re.match(r"([a-zA-Z]+)(\d+)", item[1]).group(2)),
            item[0]
        ) if re.match(r"([a-zA-Z]+)(\d+)", item[1]) else (item[1], item[0])
    )
)

print(f"Cat : {sum(1 for code in data.values() if code.startswith('Cat'))}")
print(f"Fox : {sum(1 for code in data.values() if code.startswith('Fox'))}")
for key, value in sorted_data.items():
    print(f"{key} : {value}")
