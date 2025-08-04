n, target = map(int, input().split())

num_list = list(map(int, input().split()))

possible_sum = [i + j + k 
                for i in num_list 
                for j in num_list 
                for k in num_list 
                if i != j and j != k and i != k]

close = 0
for sum in possible_sum: 
    if close < sum and sum <= target: 
        close = sum
print(close)