citations = [4, 4, 1]

def solution(citations):
    citations.sort(reverse=True)
    if citations[-1] >= 1000: 
        return 1000
    if citations[0] <= 1: 
        return citations[0]
    for idx in range(1, len(citations)): 
        for h in range(citations[idx - 1] , citations[idx], -1): 
            if idx >= h: 
                return h
    for h in range(citations[-1], 0, -1): 
        if len(citations) >= h: 
            return h
    return 0

def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution2(citations))