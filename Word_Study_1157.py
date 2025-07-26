alphabet = [0 for _ in range(26)]
word = input().upper()
for w in word: 
    alphabet[ord(w)-65] += 1

offen = 0
for alp in alphabet: 
    if offen < alp: 
        offen = alp
dup = False
m_alp = ''
for i in range(26): 
    if dup and offen == alphabet[i]: 
        print('?')
        break
    elif offen == alphabet[i]: 
        dup = True
        m_alp = chr(i+65)
else: 
    print(m_alp)