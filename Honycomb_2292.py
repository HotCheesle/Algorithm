n = int(input())

deps = 1
cutline = 1
while n > cutline: 
    cutline += deps*6
    deps += 1
print(deps)