import sys

arg_input = sys.argv[1]


with open(arg_input, 'r') as f:
    count = 0
    for l in f.readlines():
        eq = l.split(':')
        r = int(eq[0])
        op = list(map(int, eq[1].strip().split(' ')))
        vals = [[op[0]]]
        i = 0
        print(f"{r} {op}")
        for o in op[1:]:
            arr = set()
            for val in vals[i]:
                a = val+o
                b = val*o
                c = int(f'{val}{o}')
                if a <= r:
                    arr.add(a)
                if b<= r:
                    arr.add(b)
                if c <= r:
                    arr.add(c)
            if op[-1] == o:
                if r in arr:
                    print("WIN")
                    count += r
                else:
                    print("FALSE")
            vals.append(arr)
            i += 1

    print(count)
