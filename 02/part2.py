from common import load_input

def is_safe(report,used_problem_dampener=False):
    print(f'Report: {report}')
    n = len(report)
    
    current = 0
    next = 1
    previous_sign = None

    while (next < n):
        diff = report[next] - report[current]
        text = f'\t{report[current]} vs {report[next]}: '

        if diff == 0:
            text+='Same value.'
            if not used_problem_dampener:
                del report[next]
                text+='Used problem dampener.'
                print(text)
                return is_safe(report, True)
            print('\tNot Safe!')
            return False
        
        # 1 means increasing
        # -1 means decreasing
        sign = -1 if diff < 0 else 1

        #First comparison for current report?
        if not previous_sign:
            previous_sign = sign

        #Change in direction?
        if not previous_sign == sign:
            text+=f'Changed direction from {previous_sign} to {sign}.'
            if not used_problem_dampener:
                text+='Used problem dampener.'
                if previous_sign == -1 and sign == 1:
                    text+=f'Removed {report[current]}.'
                    del report[current]
                elif previous_sign == 1 and sign == -1:
                    text+=f'Removed {report[next]}.'
                    del report[next]
                print(text)
                return is_safe(report, True)
            print('\tNot Safe!')
            return False

        if abs(diff) < 1 or abs(diff) > 3:
            text+='diff <1 or >3.'
            if not used_problem_dampener:
                text+='Used problem dampener.'
                if report[next] > report[current]:
                    text+=f'Removed {report[current]}.'
                    del report[next]
                else:
                    text+=f'Removed {report[next]}.'
                    del report[current]
                print(text)
                return is_safe(report, True)
            print('\tNot Safe!')
            return False
        current = next
        next+=1
        text+='pass'
        print(text)
    print('\tSafe!')
    return True

reports = load_input()
#reports = [[7,6,4,2,1], [1, 2, 7, 8, 9], [9,7,6,2,1], [1,3,2,4,5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
#reports =[[1, 1, 2, 3, 4]]
#reports=[[1, 2, 3, 3, 4]]
safe_report_count = 0

for report in reports:
    if is_safe(report):
        safe_report_count+=1

print(f'The result for part 2 is {safe_report_count}')
print(f'Unsafe report count is {len(reports) - safe_report_count}')