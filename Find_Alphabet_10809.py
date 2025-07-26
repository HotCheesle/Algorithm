string = input()
length = 0
for s in string: 
    length += 1
alphabet = list(-1 for _ in range(26))

for i in range(length):
    alp = ord(string[i]) - 97
    if alphabet[alp] == -1: 
        alphabet[alp] = i

for a in alphabet: 
    print(a, end=' ')