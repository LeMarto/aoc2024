from common import load_input

def calculate(mul:str):
    cleaned:str = mul.replace('mul(', '').replace(')', '')
    splitted=cleaned.split(',')
    casted = list(map(lambda x: int(x), splitted))
    total = 1
    for n in casted:
        total*=n
    return total

def check_second_number_or_parenthesys(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        next_function = check_second_number_or_parenthesys
    elif value == ')':
        acum+=value
        mul_list.append(acum)
        processed.append(proc)
        acum=''
        proc=''
        next_function = check_m
    else:
        next_function = check_second_number_or_parenthesys
    mul_list.append(acum)
    processed.append(proc)
    return [mul_list, next_function, processed]   

def check_second_number(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        next_function = check_second_number_or_parenthesys
    else:
        next_function = check_second_number
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]   
    
def check_number_or_comma(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        next_function = check_number_or_comma
    elif value == ',':
        acum+=value
        next_function = check_second_number
    else:
        next_function = check_number_or_comma
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]    
    
def check_first_number(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        next_function = check_number_or_comma
    else:
        next_function = check_first_number
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]
    
def check_op(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value == '(':
        acum+=value
        next_function = check_first_number
    else:
        next_function = check_op
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]
    
def check_l(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value == 'l':
        acum+=value
        next_function = check_op
    else:
        next_function = check_l
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]

def check_u(value, mul_list:list[str], processed:list[str]):
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value=='m' and len(acum) > 0 and not acum[-1:] == ')':
        acum = 'm'
        next_function = check_u
    elif value == 'u':
        acum+=value
        next_function = check_l
    else:
        next_function = check_u
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]

def check_m(value, mul_list:list[str], processed:list[str]):
    if len(mul_list) == 0:
        mul_list.append('')
    if len(processed) == 0:
        processed.append('')
    acum = mul_list.pop()
    proc = processed.pop()
    proc+=value
    if value == 'm':
        acum+=value
        next_function = check_u
    else:
        next_function = check_m
    processed.append(proc)
    mul_list.append(acum)
    return [mul_list, next_function, processed]

def parse_muls(line:str):
    muls = []
    processed = []
    next = check_m
    for char in line:
        muls, next, processed = next(char, muls, processed)
    first = muls.pop()
    #Check if first element is completed or not
    if len(first) > 0:
        muls.append(first)

    return [muls, processed]

if __name__=='__main__':
    line_number = 1
    total = 0
    for line in load_input():
        line_total = 0
        muls, processed = parse_muls(line)
        print(f'\nline {line_number} contains the following muls:')
        for i in range(len(muls)):
            mul = muls[i]
            proc = processed[i]
            mul_result = calculate(mul)
            print(f'\t{mul} <- \"{proc}\" = {mul_result}')
            line_total+=mul_result
        print(f'The line subtotal is: {line_total}')
        total+=line_total
        line_number+=1     
    print(f'The result for part 1 is {total}')