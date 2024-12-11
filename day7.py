import sys

arg_input = sys.argv[1]

with open(arg_input, 'r') as f:
    for l in f.readlines():
        eq = l.split(':')
        r = int(eq[0])
        op = list(map(int, eq[1].strip().split(' ')))
        tmp = op[0]
        print(f"{r} {op}")
        for o in op[1:]:
            if op[-1] == o:
                if tmp * o == r:
                    print(f"WIN({r}) {tmp} * {o}")
                elif tmp + o == r:
                    print(f"WIN({r}) {tmp} + {o}")
                else:
                    print(f"something wrong {tmp*o} {tmp+o}\n")
            elif tmp * o > r:
                print(f" {tmp} + {o}")
                tmp += o
            else:
                print(f" {tmp} * {o}")
                tmp *= o
