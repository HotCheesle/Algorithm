def check_board(row, col): 
    w_cnt, b_cnt = 0, 0
    for r in range(8): 
        for c in range(8): 
            if (r + c) % 2 == 0: 
                if board[row+r][col+c] == 'B': 
                    w_cnt += 1
                else: 
                    b_cnt += 1
            else: 
                if board[row+r][col+c] == 'W': 
                    w_cnt += 1
                else: 
                    b_cnt += 1
    return min(w_cnt, b_cnt)

height, width = map(int, input().split())
board = list(input() for _ in range(height))

min_cnt = height * width
for row in range(height - 7): 
    for col in range(width - 7): 
        min_cnt = min(min_cnt, check_board(row, col))
print(min_cnt)