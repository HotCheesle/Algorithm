up, down, height = map(int, input().split())

day_up = up - down
height -= up
days = (height // day_up) + 1
if height % day_up != 0: days += 1
print(days)