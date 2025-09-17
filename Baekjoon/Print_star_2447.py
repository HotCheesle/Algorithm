def print_sierpinski_carpet(rdepth, N, rofs, tot, hold): 
    if N == 3: 
        print_row(rdepth, exp, tot, rofs, 0, tot, False)
        print_row(rdepth, exp, tot, rofs+1, 0, tot, False)
        print_row(rdepth, exp, tot, rofs+2, 0, tot, False)
    else: 
        if hold: 
            print_sierpinski_carpet(rdepth, N//3, rofs, tot, True)
            print_sierpinski_carpet(rdepth, N//3, rofs+N//3, tot, True)
            print_sierpinski_carpet(rdepth, N//3, rofs+(N//3)*2, tot, True)
        else: 
            print_sierpinski_carpet(rdepth-1, N//3, rofs, tot, False)
            print_sierpinski_carpet(rdepth, N//3, rofs+N//3, tot, True)
            print_sierpinski_carpet(rdepth-1, N//3, rofs+(N//3)*2, tot, False)

def print_row(rdepth, cdepth, N, row, cofs, tot, hold):
    if N == 3: 
        depth = min(rdepth, cdepth)
        for rpow in range(1, depth): 
            for cpow in range(1, depth): 
                if row // 3**rpow % 3 == 1 and cofs // 3**cpow % 3 == 1: 
                    print('   ', end='')
                    return
        else: 
            if row % 3 == 1: 
                print('* *', end='')
            else: 
                print('***', end='')
        if cofs == tot-3: 
            print()
    else: 
        if hold: 
            print_row(rdepth, cdepth, N//3, row, cofs, tot, True)
            print_row(rdepth, cdepth, N//3, row, cofs+N//3, tot, True)
            print_row(rdepth, cdepth, N//3, row, cofs+(N//3)*2, tot, True)
        else: 
            print_row(rdepth, cdepth-1, N//3, row, cofs, tot, False)
            print_row(rdepth, cdepth, N//3, row, cofs+N//3, tot, True)
            print_row(rdepth, cdepth-1, N//3, row, cofs+(N//3)*2, tot, False)

N = int(input())
exp, n = 0, N
while n != 1: 
    exp += 1
    n //= 3
print_sierpinski_carpet(exp, N, 0, N, False)

# ***
# * *
# ***

# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********