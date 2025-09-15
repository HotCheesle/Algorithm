def div(N, rofs, cofs): 
    global count
    num_set = set()
    for row in range(rofs, rofs+N): 
        for col in range(cofs, cofs+N): 
            num_set.add(paper[row][col])
            if len(num_set) != 1: 
                break
        else: 
            continue
        break
    else: 
        count[num_set.pop()] += 1
        return
    Ndiv = N // 3
    for i in range(3): 
        for j in range(3): 
            div(Ndiv, rofs+(Ndiv*i), cofs+(Ndiv*j))

N = int(input())
paper = list(list(map(int, input().split())) for _ in range(N))
count = [0, 0, 0]
div(N, 0, 0)
for i in range(-1, 2): 
    print(count[i])