from heapq import heappush, heappop

pq = []
jobs = [[0, 3], [5, 9], [6, 5]]
jobs.sort(key=lambda x: x[0])

t = 0
idx = 0
answer = 0

while idx < len(jobs) or pq:
    if not pq and jobs[idx][0] > t: 
        t = jobs[idx][0]
    while idx < len(jobs) and jobs[idx][0] <= t: 
        heappush(pq, ((jobs[idx][1]<<20) + (jobs[idx][0]<<10) + idx))
        idx += 1
    job = heappop(pq)
    t += job>>20
    answer += t - ((job>>10) & 1023)

answer //= len(jobs)
print(answer)

