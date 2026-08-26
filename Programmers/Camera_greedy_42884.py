# routes = [[0, 6], [2, 4], [5, 9], [7, 19], [8, 10], [11, 16], [14, 21]]
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

routes.sort()
cam_st = routes[0][1]
cam_cnt = 0

for r in routes: 
    if r[0] <= cam_st: 
        if r[1] < cam_st: 
            cam_st = r[1]
    else: 
        cam_cnt += 1
        cam_st = r[1]

cam_cnt += 1
