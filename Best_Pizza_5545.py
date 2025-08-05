N = int(input())
dough, topping = map(int, input().split())
dough_cal = int(input())
topping_cal = []
for _ in range(N): 
    topping_cal.append(int(input()))

tot_cal, tot_price = dough_cal, dough
price_per_cal = int(tot_cal / tot_price)
pre_p_per_c = 0 # 이전값과 비교하기위해 이전값 저장할 변수

while pre_p_per_c <= price_per_cal: # 토핑 추가로 값 다시 떨어질 때 까지
    pre_p_per_c = price_per_cal 
    max_top_cal = 0
    for cal in topping_cal: # 가장 큰 칼로리의 토핑을 추가함
        if max_top_cal < cal: 
            max_top_cal = cal
    if max_top_cal == 0: break # 모든 토핑 선택 시 정지
    topping_cal.remove(max_top_cal) # 토핑 리스트에서 제외
    tot_cal += max_top_cal # 총 칼로리에 토핑 칼로리 더하기
    tot_price += topping # 총 가격에 토핑 가격 더하기
    price_per_cal = int(tot_cal / tot_price)

print(pre_p_per_c)