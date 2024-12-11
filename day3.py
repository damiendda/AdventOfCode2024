import sys
import re

arg_input = sys.argv[1]

with open(arg_input, 'r') as f:
    summ = 0
    enabled = True
    for l in f:
        res = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\)|don\'t\(\))', l)
        print(res)
        for i in res:
            if i[2] == "do()":
                enabled = True
            elif i[2] == "don't()":
                enabled = False
            elif enabled:
                print(f"mul({int(i[0])},{int(i[1])})")
                summ += int(i[0]) * int(i[1])
    print(summ)