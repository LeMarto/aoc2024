from common import load_input

def is_uniform(report):
    n = len(report)
    assert n > 1, "report cant have less than 2 levels!"
    current = 0
    next = 1
    previous_sign = 0
    while (next < n):
        diff = report[next] - report[current]
        if diff == 0:
            return False
        sign = -1 if diff < 0 else 1
        current = next
        next+=1
        if previous_sign == 0:
            previous_sign = sign
            continue
        if not previous_sign == sign:
            return False
    return True

def diff_in_range(report):
    n = len(report)
    assert n > 1, "report cant have less than 2 levels!"
    current = 0
    next = 1
    while (next < n):
        diff = abs(report[next] - report[current])
        if diff < 1 or diff > 3:
            return False
        current = next
        next+=1
    return True

reports = load_input()
safe_report_count = 0
for report in reports:
    if is_uniform(report) and diff_in_range(report):
        safe_report_count+=1

print(f'The result for part 1 is {safe_report_count}')