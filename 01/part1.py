left = []
right = []
with open('input', 'r') as file:
    for line in file:
        splitted_line = line.split('   ')
        left_number = int(splitted_line[0])
        right_number = int(splitted_line[1].replace('\n',''))
        left.append(left_number)
        right.append(right_number)

left.sort()
right.sort()

n = len(left)

distances = []

for x in range(n):
    left_number = left.pop()
    right_number = right.pop()
    distance = abs(left_number-right_number)
    distances.append(distance)

total = 0
for d in distances:
    total+=d

print(f'Answer: {total}')