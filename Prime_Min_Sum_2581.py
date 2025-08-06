st = int(input())
ed = int(input())

scope = [i for i in range(st, ed+1)]
rm_num = []
primes = [i for i in range(2, 101)]
for n in range(2, 11): 
    np = n*2
    while np <= 100: 
        try: 
            primes.remove(np)
            np += n
        except: 
            np += n
            continue

for p in primes: 
    np = p*2
    while np <= ed: 
        try: 
            scope.remove(np)
            np += p
        except: 
            np += p
            continue

try:
    scope.remove(1)
except: 
    pass

if len(scope) == 0: 
    print('-1')
else: 
    print(sum(scope))
    print(scope[0])
