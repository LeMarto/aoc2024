from common import load_input

left,right = load_input()

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

print(f'The result for part 1 is {total}')