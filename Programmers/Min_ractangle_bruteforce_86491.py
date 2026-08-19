sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

large, small = 0, 0

for card in sizes: 
    large = max(large, max(card))
    small = max(small, min(card))

print(large * small)