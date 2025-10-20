N = int(input())
num_list = list(0 for _ in range(N))
for i in range(N): 
    num_list[i] = int(input())
num_list.sort()
mean = round(sum(num_list) / N)
mid = num_list[N//2]
most = {}
for n in num_list: 
    if n not in most: 
        most[n] = 1
    else: 
        most[n] += 1
most_cnt = max(list(most.values()))
most_nums = []
for key, value in most.items(): 
    if value == most_cnt: 
        most_nums.append(key)
most_nums.sort()
if len(most_nums) == 1: 
    most_num = most_nums[0]
else: 
    most_num = most_nums[1]
arange = num_list[N-1] - num_list[0]

print(mean)
print(mid)
print(most_num)
print(arange)