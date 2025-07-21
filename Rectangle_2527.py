import sys

ans_buffer = list()

for i in range(4): 
    x_s1, y_s1, x_e1, y_e1, x_s2, y_s2, x_e2, y_e2 = map(int, sys.stdin.readline().split())

    part_x = False
    only_point_x = False
    none_x = False
    part_y = False
    only_point_y = False
    none_y = False

    if (x_s1 <= x_s2 and x_s2 < x_e1) or (x_s1 < x_e2 and x_e2 <= x_e1): 
        part_x = True
    elif (x_s2 <= x_s1 and x_s1 < x_e2) or (x_s2 < x_e1 and x_e1 <= x_e2): 
        part_x = True
    elif (x_s1 == x_e2) or (x_e1 == x_s2): 
        only_point_x = True
    elif (x_s1 > x_e2) or (x_e1 < x_s2): 
        none_x = True
    elif (x_s2 > x_e1) or (x_e2 < x_s1): 
        none_x = True
        
    if (y_s1 <= y_s2 and y_s2 < y_e1) or (y_s1 < y_e2 and y_e2 <= y_e1): 
        part_y = True
    elif (y_s2 <= y_s1 and y_s1 < y_e2) or (y_s2 < y_e1 and y_e1 <= y_e2): 
        part_y = True
    elif (y_s1 == y_e2) or (y_e1 == y_s2): 
        only_point_y = True
    elif (y_s1 > y_e2) or (y_e1 < y_s2): 
        none_y = True
    elif (y_s2 > y_e1) or (y_e2 < y_s1): 
        none_y = True
    
    if part_x and part_y: ans_buffer.append("a")
    elif (only_point_x and part_y) or (only_point_y and part_x): ans_buffer.append("b")
    elif only_point_x and only_point_y: ans_buffer.append("c")
    elif none_x or none_y: ans_buffer.append("d")
    
for i in range(4): 
    print(ans_buffer[i])