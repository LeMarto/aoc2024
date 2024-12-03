def load_input():
    reports = []
    with open('input', 'r') as file:
        for report in file:
            level_strings = report.split(' ')
            levels = list(map(lambda x: int(x), level_strings))
            reports.append(levels)

    return reports