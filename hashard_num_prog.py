def solution(x):
    tot = 0
    n = x
    while n != 0: 
        tot += n % 10
        n //= 10
    if x % tot == 0: 
        return True
    else: 
        return False