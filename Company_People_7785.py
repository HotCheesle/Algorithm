n = int(input())

people_set = set()

for i in range(n): 
    name, log = input().split()
    if log == 'enter': 
        people_set.add(name)
    else: 
        people_set.remove(name)

sort_list = sorted(list(people_set), reverse=True)
for n in sort_list: 
    print(n)