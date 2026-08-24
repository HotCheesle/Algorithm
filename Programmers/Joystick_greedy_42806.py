name = "BBBABBB"

# 일단 순회 해서 첫 자리를 제외하고 연속된 A를 찾음
# 그 A들을 피하도록 했을 때 짧은쪽 > 긴쪽 으로 갔을 때 (2짧 + 긴) 이게 가장 걸로 move

long_a = []
st = None
for i in range(1, len(name)): 
    if name[i] == "A": 
        if not st: 
            st = i
    else: 
        if st: 
            long_a.append((st, i))
            st = None

if st: 
    long_a.append((st, len(name)))

min_mv = 31
if long_a: 
    for l in long_a: 
        mv = 2 * min(l[0] - 1, len(name) - l[1]) + max(l[0] - 1, len(name) - l[1])
        if min_mv > mv: 
            min_mv = mv

if min_mv > len(name) - 1: 
    min_mv = len(name) - 1

for c in name: 
    min_mv += min(ord(c) - 65, 91 - ord(c))

print(min_mv)