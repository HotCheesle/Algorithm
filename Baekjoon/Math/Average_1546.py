n = int(input())

score_list = list(map(int, input().split()))
max_score = 0
for s in score_list: 
    if max_score < s: 
        max_score = s
    
ch_score_list = [(s / max_score) * 100 for s in score_list]

tot = 0
for ch in ch_score_list: 
    tot += ch

print(tot/n)