from heapq import heapify, heappush, heappop

scoville = [1, 2, 3, 9, 10, 12]
K = 7

heapify(scoville)

mix_cnt = 0
while scoville[0] < K: 
    if len(scoville) <= 1: 
        print(-1)
    low = heappop(scoville)
    low_2nd = heappop(scoville)
    heappush(scoville, low + (low_2nd * 2))
    mix_cnt += 1
print(mix_cnt)