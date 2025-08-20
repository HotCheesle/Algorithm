string = input()

string = string.replace('c=', 'c')
string = string.replace('c-', 'c')
string = string.replace('dz=', 'd')
string = string.replace('d-', 'd')
string = string.replace('lj', 'l')
string = string.replace('nj', 'n')
string = string.replace('s=', 's')
string = string.replace('z=', 'z')

length = 0
for s in string: 
    length += 1
print(length)