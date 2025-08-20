string, num_sys = input().split()
num_sys = int(num_sys)

deci = 0
for i in range(len(string) - 1, -1, -1):
    try: 
        num = int(string[i])
    except: 
        num = ord(string[i]) - 55
    deci += num * (num_sys ** (len(string) - i - 1))

print(deci)