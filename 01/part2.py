import bisect
from common import load_input

def count_ocurrences(list, element):
    index = bisect.bisect_left(list, element)
    ocurrences = 0
    if index < len(list) and list[index] == element:
        start = index
        while index < len(list) and list[index] == element:
            ocurrences+=1
            index+=1
    return ocurrences

left,right = load_input()

similarity_score = 0

for n in left:
    ocurrences = count_ocurrences(right, n)
    similarity_score += n*ocurrences

print(f'The result for part 2 is {similarity_score}')