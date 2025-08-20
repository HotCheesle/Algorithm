line = set()
N = int(input())
num_list = list(map(int, input().split()))
for num in num_list: 
    line.add(num)

line = list(line)
sorted_line = sorted(line)

count = 0
maping = {}
for k in sorted_line: 
    maping[k] = count
    count += 1

for k in num_list: 
    print(f'{maping[k]} ', end='')
print()