genres, plays = ["classic", "pop", "classic", "classic", "pop", "hiphop"], [500, 600, 500, 600, 2500, 10000]

best_album = dict()
g_rank = dict()
for idx in range(len(genres)): 
    if best_album.get(genres[idx]): 
        if best_album[genres[idx]][0][0] < plays[idx]:
            best_album[genres[idx]][1] = best_album[genres[idx]][0]
            best_album[genres[idx]][0] = (plays[idx], idx)
        elif (best_album[genres[idx]][1] is None 
            or best_album[genres[idx]][1][0] < plays[idx]): 
                best_album[genres[idx]][1] = (plays[idx], idx)
        g_rank[genres[idx]] += plays[idx]
    else: 
        best_album[genres[idx]] = [(plays[idx], idx), None]
        g_rank[genres[idx]] = plays[idx]
    print(best_album)

g_list = list(g_rank.items())
g_list.sort(key=lambda g: g[1], reverse=True)

answer = []
for g in g_list: 
    answer.append(best_album[g[0]][0][1])
    if best_album[g[0]][1] is None:
        continue
    answer.append(best_album[g[0]][1][1])

print(answer)