nums = [3, 3, 3, 2, 2, 2]

d = set()
for n in nums: 
    d.add(n)

answer = min(int(len(nums)/2), len(d))
print(answer)