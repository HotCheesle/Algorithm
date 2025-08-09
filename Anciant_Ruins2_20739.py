T = int(input())
for tc in range(1, T+1): 
    height, width = map(int, input().split())
    picture = list(list(map(int, input().split())) for _ in range(height))
    max_length = 0
    for row in range(height): 
        length = 0
        for col in range(width): 
            if picture[row][col] == 1: 
                length += 1
            else: 
                if length > 1 and max_length < length: 
                    max_length = length
                length = 0
        if length > 1 and max_length < length: 
            max_length = length
        length = 0
    for col in range(width): 
        length = 0
        for row in range(height): 
            if picture[row][col] == 1: 
                length += 1
            else: 
                if length > 1 and max_length < length: 
                    max_length = length
                length = 0
        if length > 1 and max_length < length: 
            max_length = length
        length = 0
    print(f'#{tc} {max_length}')