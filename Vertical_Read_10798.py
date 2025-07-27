from itertools import zip_longest as zipl

mat = []
for _ in range(5): 
    mat.append(list(input()))

ziped = list(zipl(mat[0], mat[1], mat[2], mat[3], mat[4], fillvalue=''))
for s in ziped: 
    for c in s: 
        print(c, end='')