numbers, target = [4, 1, 2, 1], 4

def dfs(nums, num, tg, idx): 
    if idx >= len(nums): 
        if num == tg: 
            return 1
        else: 
            return 0
    return dfs(nums, num+nums[idx], tg, idx+1) + dfs(nums, num-nums[idx], tg, idx+1)

print(dfs(numbers, 0, target, 0))