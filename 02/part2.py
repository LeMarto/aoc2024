from common import load_input

def is_safe(report):
    n = len(report)    
    current = 0
    next = 1
    previous_sign = None

    while (next < n):
        diff = report[next] - report[current]
        if diff == 0:
            return False
        
        # 1 means increasing
        # -1 means decreasing
        sign = -1 if diff < 0 else 1

        #First comparison for current report?
        if not previous_sign:
            previous_sign = sign

        #Change in direction?
        if not previous_sign == sign:
            return False

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        current = next
        next+=1
    return True

reports = load_input()
safe_report_count = 0

for report in reports:    
    if is_safe(report):
        safe_report_count+=1
    else:
        for i in range(len(report)):
            copy = report.copy()
            del copy[i]
            if is_safe(copy):
                safe_report_count+=1
                break

print(f'The result for part 2 is {safe_report_count}')