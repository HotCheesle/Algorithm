from collections import deque

bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]

t = 0
truck_weights = deque(truck_weights)
bridge = deque()
while truck_weights or bridge: 
    t += 1
    if bridge and bridge[0][1] == t: 
        weight += bridge[0][0]
        bridge.popleft()
    if truck_weights and truck_weights[0] <= weight: 
        weight -= truck_weights[0]
        bridge.append((truck_weights.popleft(), t + bridge_length))
print(t)