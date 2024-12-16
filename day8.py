import sys

arg_input = sys.argv[1]


with open(arg_input, 'r') as f:
    ants = {}
    i = 0
    ati = []
    iMax = 0 
    jMax = 0
    mmap = []
    for l in f.readlines():
        mmap.append(list(l.strip()))
    
    iMax = len(mmap)
    jMax = len(mmap[0])

    cout = set()
    cout2 = set()
    result = 0
    for l in mmap:
        j = 0
        for e in l:
            if e != '.' and e != '#' and e != "@":
                if e not in ants:
                    ants[e] = []
                else:
                    print()
                    for ant in ants[e]:
                        x, y = ant
                        rx, ry = (i - (x - i), j - (y - j))
                        xr, yr = (x - (i - x), y - (j - y))
                        # Part 1
                        if rx >= 0 and rx < iMax and ry >= 0 and ry < jMax:
                            cout.add((rx,ry))
                            print(f"{ant} -> ({i}, {j}) {(rx, ry)} # {e}")
                            if mmap[rx][ry] == '.':
                                mmap[rx][ry] = "#"
                        if xr >= 0 and xr < iMax and yr >= 0 and yr < jMax:
                            cout.add((xr,yr))
                            print(f"({i}, {j}) -> {ant} {(xr, yr)} # {e}")
                            if mmap[xr][yr] == '.':
                                mmap[xr][yr] = "#"
                        # Part 2
                        k = 0
                        m = i - (k * (x-i))
                        n = j - (k * (y-j))
                        while m >= 0 and m < iMax and n >= 0 and n < jMax:
                            cout2.add((m,n))
                            if mmap[m][n] == '.':
                                mmap[m][n] = "#"
                            k += 1
                            m = i - (k * (x-i))
                            n = j - (k * (y-j))
                        k = 0
                        m = x - (k * (i-x))
                        n = y - (k * (j-y))
                        while m >= 0 and m < iMax and n >= 0 and n < jMax:
                            cout2.add((m,n))
                            if mmap[m][n] == '.':
                                mmap[m][n] = "#"
                            k += 1
                            m = x - (k * (i-x))
                            n = y - (k * (j-y))

                ants[e].append((i,j))
            j += 1
        i += 1

    for l in mmap:
        print("".join(l))

    print(len(cout))
    print(len(cout2))
