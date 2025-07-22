import sys

dwarfs = []
real_dwarf = []
for i in range(9): 
    dwarfs.append(int(sys.stdin.readline()))

tot = sum(dwarfs)
dif = tot - 100

for d in dwarfs: 
    if d >= dif: 
        real_dwarf.append(d)
        dwarfs.remove(d)

fake = [[x, y] for x in dwarfs for y in dwarfs if x+y == dif and not x == y]
    
dwarfs.remove(fake[0][0])
dwarfs.remove(fake[0][1])

for d in dwarfs: 
    real_dwarf.append(d)

real_dwarf.sort()

for rd in real_dwarf:
    print(rd)