people, limit = [10, 10, 10, 10], 10
people.sort()

boat = 0
light, heavy = 0, len(people) - 1

while light < heavy: 
    if people[light] + people[heavy] <= limit: 
        boat += 1
        light += 1
        heavy -= 1
    else: 
        boat += 1
        heavy -= 1

if light == heavy: 
    boat += 1

print(boat)