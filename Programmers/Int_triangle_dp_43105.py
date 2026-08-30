triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

if len(triangle) == 1: 
    print(triangle[0][0])

for lv in range(1, len(triangle)): 
    for n in range(len(triangle[lv])): 
        if n == 0: 
            triangle[lv][n] += triangle[lv-1][n]
        elif n == len(triangle[lv])-1: 
            triangle[lv][n] += triangle[lv-1][n-1]
        else: 
            if triangle[lv-1][n-1] >= triangle[lv-1][n]: 
                triangle[lv][n] += triangle[lv-1][n-1]
            else: 
                triangle[lv][n] += triangle[lv-1][n]

print(max(triangle[-1]))