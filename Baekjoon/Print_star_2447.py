def print_sierpinski_carpet(N, row, col, blank):
    """
    (블럭길이, 행, 열, 전체길이, 빈칸여부)
    """
    if N == 1: 
        if blank: 
            sierpinski_carpet[row][col] = ' '
        else: 
            sierpinski_carpet[row][col] = '*'
    else: 
        for rb in range(3): 
            for cb in range(3): 
                next_blank = blank
                if rb == 1 and cb == 1: next_blank |= True
                print_sierpinski_carpet(N//3, row+(rb*N//3), col+(cb*N//3), next_blank)


N = int(input())
sierpinski_carpet = list(['']*N for _ in range(N))
print_sierpinski_carpet(N, 0, 0, False)
for rows in sierpinski_carpet: 
    print(''.join(rows))
