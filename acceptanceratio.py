import re
import math

def get_float(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

def get_int(x):
    return re.findall('\d+',x)

accept_y = []
MDstep_x = []


with open("NCtermdata.txt") as f:
    for line in f:
        if "Acceptance Ratio" in line:
            accept_y.append(get_float(line))
        if "Running blues with" in line:
            y = get_int(line)
            MDstep_x.append(int(y[0]))

print(accept_y)
print(MDstep_x)

