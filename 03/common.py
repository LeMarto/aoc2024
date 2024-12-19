import os
def load_input():
    print(os.getcwd())
    lines = []
    with open('input', 'r') as file:
        for line in file:
            lines.append(line)
    return lines