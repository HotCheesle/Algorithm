mat = []
for _ in range(9): 
    mat.append(list(map(int, input().split())))

max_val = 0
y_m, x_m = 0, 0
for y in range(9): 
    for x in range(9): 
        if max_val < mat[y][x]: 
            max_val = mat[y][x]
            y_m = y
            x_m = x

print(max_val)
print(str(y_m + 1) + ' ' + str(x_m + 1))