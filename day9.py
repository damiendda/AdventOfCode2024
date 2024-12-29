import sys
import itertools

arg_input = sys.argv[1]

def p1(s1):
    i = 0 # '.' pointer
    j = len(s1)-1 # 'id' pointer
    count = 0
    while j > i and j > -1:
        if not s1[i] or s1[i] != '.':
            if s1[i] != '.':
                count += i * int(s1[i])
            i += 1
        elif not s1[j] or s1[j] == '.':
            j -= 1
        else:
            s1[i] = s1[j]
            count += i * int(s1[i])
            s1[j] = '.'
            j -= 1
            i += 1
    while(s1[i] != '.'):
        count += int(s1[i]) * i
        i += 1
    print(count)

def printIds(ids, size):
    lastSrc = 0
    count = 0
    res = ['.'] * (size + 10)
    for id, tu in ids.items():
        for i in range(tu[1]):
            count += id * (tu[0]+i)
            res[tu[0]+i] = str(id)
    #print("".join(res))
    print(f"sum: {count}")

def p2(ids, gaps):
    for k in sorted(ids.keys(), reverse=True):
        it_gaps = iter(gaps)
        for tu in it_gaps:
            if ids[k][1] <= tu[1] and ids[k][0] > tu[0]:
                ids[k][0] = tu[0]
                if ids[k][1] == tu[1]:
                    gaps.remove(tu)
                else:
                    tu[0] += ids[k][1]
                    tu[1] -= ids[k][1]
                break
            


with open(arg_input, 'r') as f:
    i = 0
    s1 = []
    ids = {}
    gaps = []
    l = f.readline().strip()
    length = 0
    cur_pos = 0
    for c in l:
        x = int(c)
        if i % 2 == 0:
            ids[int(i/2)] = [cur_pos, x]
            s1.extend(list(x * [f"{int(i/2)}"]))
        else:
            if c != "0":
                gaps.append([cur_pos, x])
            s1.extend(list(x *'.'))
        i += 1
        cur_pos += x
        length += x
    p1(s1.copy())
    p2(ids, gaps)
    printIds(ids, length)
