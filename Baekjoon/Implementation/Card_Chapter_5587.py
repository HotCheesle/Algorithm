N = int(input())
cards = set(range(1, N*2 + 1))
sg_list = set()
for _ in range(N): 
    sg_list.add(int(input()))
gs_list = cards.difference(sg_list)

field = min(sg_list)
sg_list.remove(field)

while sg_list and gs_list: 
    for card in range(field+1, N*2+1): 
        if card in gs_list: 
            field = card
            gs_list.remove(card)
            break
    else: 
        field = min(sg_list)
        sg_list.remove(field)
        continue
    if len(gs_list) == 0:
        break
    for card in range(field+1, N*2+1): 
        if card in sg_list: 
            field = card
            sg_list.remove(card)
            break
    else: 
        field = 0

print(len(gs_list))
print(len(sg_list))

