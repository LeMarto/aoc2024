def load_input():
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
        return [left, right]