from pprint import pprint as pp

rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8

borad = list(list(0 for _ in range(10)) for _ in range(10))
for r in rectangle: 
    for row in range(r[1], r[3]+1): 
        for col in range(r[0], r[2]+1): 
            if borad[row][col] != 2 and (row in (r[1], r[3]) or  col in (r[0], r[2])): 
                borad[row][col] = 1
            else: 
                borad[row][col] = 2

pp(borad)
