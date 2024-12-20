from common import load_input
from pydantic import BaseModel
from typing import Callable

class State(BaseModel):
    mul_list:list[str]=[]
    processed:list[str]=[]
    ignoring:bool=False
    next:Callable[[str, 'State'], 'State']=None

def record_processed(value:str, state:State):
    if len(state.processed) == 0:
        state.processed.append('')
    proc = state.processed.pop()
    proc+=value
    state.processed.append(proc)
    
def calculate(mul:str):
    cleaned:str = mul.replace('mul(', '').replace(')', '')
    splitted=cleaned.split(',')
    casted = list(map(lambda x: int(x), splitted))
    total = 1
    for n in casted:
        total*=n
    return total

def check_second_number_or_parenthesys(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        state.next = check_second_number_or_parenthesys
    elif value == ')':
        #check if ignoring or not
        acum+=value
        if not state.ignoring:
            state.mul_list.append(acum)
        acum=''
        state.processed.append('')
        state.next = start
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)
    
    return state

def check_second_number(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        state.next = check_second_number_or_parenthesys
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)
    
    return state
    
def check_number_or_comma(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        state.next = check_number_or_comma
    elif value == ',':
        acum+=value
        state.next = check_second_number
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)

    return state 
    
def check_first_number(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value in ['0','1','2','3','4','5','6','7','8','9']:
        acum+=value
        state.next = check_number_or_comma
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)

    return state
    
def check_op(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == '(':
        acum+=value
        state.next = check_first_number
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)

    return state
    
def check_l(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 'l':
        acum+=value
        state.next = check_op
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)

    return state

def check_u(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 'u':
        acum+=value
        state.next = check_l
    else:
        #restart discarding acumulated
        acum=''
        state.next = start

    state.mul_list.append(acum)

    return state

def check_m(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    if len(state.mul_list) == 0:
        state.mul_list.append('')

    acum = state.mul_list.pop()

    if value == 'm':
        acum+=value
        state.next = check_u
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_dont_cl_par(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    state.mul_list.pop()

    if value == ')':
        state.processed.append('')
        #set ignore to false!
        state.ignoring = True

    state.nex = start
    state.mul_list.append('')
    
    return state 

def check_dont_op_par(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == '(':
        acum+=value
        state.next = check_dont_cl_par
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_do_cl_par(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    state.mul_list.pop()

    if value == ')':
        state.processed.append('')
        #set ignore to false!
        state.ignoring = False

    state.next = start
    state.mul_list.append('')

    return state

def check_do_op_par(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == '(':
        acum+=value
        state.next = check_do_cl_par
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_t(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 't':
        acum+=value
        state.next = check_dont_op_par
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_n(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 'n':
        acum+=value
        state.next= check_t
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_do_or_dont(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == '(':
        acum+=value
        state.next = check_do_op_par
    elif value == 'n':
        acum+=value
        state.next = check_n
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_o(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 'o':
        acum+=value
        state.next = check_do_or_dont
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def check_d(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    acum = state.mul_list.pop()

    if value == 'd':
        acum+=value
        state.next = check_o
    else:
        state.next = start
    
    state.mul_list.append(acum)

    return state

def start(value:str, state:State) -> State:
    record_processed(value=value, state=state)

    if len(state.mul_list) == 0:
        state.mul_list.append('')

    if value == 'd':
        return check_d(value=value, state=state)
    elif value == 'm':
        return check_m(value=value, state=state)

def parse_muls(line:str, state:State) -> State:
    for char in line:
        state = state.next(value=char, state=state)
    first = state.muls.pop()
    #Check if first element is completed or not
    if len(first) > 0:
        state.muls.append(first)

    return state

if __name__=='__main__':
    state=State()
    state.next = start
    line_number = 1
    total = 0
    for line in load_input():
        line_total = 0
        state = parse_muls(line, state)
        print(f'\nline {line_number} contains the following muls:')
        for i in range(len(state.muls)):
            mul = state.muls[i]
            proc = state.processed[i]
            mul_result = calculate(mul)
            print(f'\t{mul} <- \"{proc}\" = {mul_result}')
            line_total+=mul_result
        print(f'The line subtotal is: {line_total}')
        total+=line_total
        line_number+=1     
        state.processed.clear()
        state.mul_list.clear()
        state.next=start
    print(f'The result for part 1 is {total}')