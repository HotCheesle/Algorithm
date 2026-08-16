prices = [1, 2, 3, 2, 3]

answer = [0 for _ in range(len(prices))]
stack = [(prices[0], 0)]
top = 0

for i in range(1, len(prices)):
    while top >= 0 and stack[top][0] > prices[i]: 
        answer[stack[top][1]] = i - stack[top][1]
        stack.pop()
        top -= 1
    stack.append((prices[i], i))
    top += 1

while stack: 
    answer[stack[top][1]] = len(prices) - 1 - stack[top][1]
    stack.pop()
    top -= 1

print(answer)