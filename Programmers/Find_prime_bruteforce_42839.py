from math import sqrt

def find_all_numbers(num_list: set, str: list, num: str, idx: int, depth: int): 
    if idx == depth: 
        if num: 
            num_list.add(int(num))
        return None

    find_all_numbers(num_list, str, num, idx + 1, depth)
    for i in range(len(str)): 
        new_str = str.copy()
        new_str.remove(str[i])
        find_all_numbers(num_list, new_str, num+str[i], idx + 1, depth)

numbers = "17"
cstr = list(numbers)
num_set = set()
answer = 0

find_all_numbers(num_set, cstr, "", 0, len(numbers))
for n in num_set: 
    if (n < 2): 
        continue
    for i in range(2, int(sqrt(n))): 
        if (n % i == 0): 
            break
    else: 
        answer += 1

print(answer)