progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]

pub = 0
answer = []
while pub < len(progresses): 
    while progresses[pub] < 100:
        for i in range(pub, len(progresses)): 
            progresses[i] += speeds[i]
    pub_cnt = 0
    while progresses[pub] >= 100: 
        pub_cnt += 1
        pub += 1
        if pub == len(progresses): 
            break
    answer.append(pub_cnt)
print(answer)