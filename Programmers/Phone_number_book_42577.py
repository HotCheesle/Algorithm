phone_book = ["97674223", "1195524421", "119"]

pb = set(phone_book)
prefix = set()
for pn in phone_book: 
    if (pn in prefix): 
        answer = False
        print(answer)
    for i in range(1, len(pn)): 
        if (pn[:i] in pb): 
            answer = False
            print(answer)
        prefix.add(pn[:i])
answer = True
print(answer)
print(prefix)