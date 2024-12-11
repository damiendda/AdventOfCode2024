import sys
from collections import defaultdict

arg_input = sys.argv[1]

with open(arg_input, 'r') as f:
    step2 = False
    count1 = 0
    count2 = 0
    rules = {}
    iteration = 0
    rules = defaultdict(lambda: [], rules)

    for l in f.readlines():
        if "\n" == l:
            step2 = True
            continue
        if step2 == False:
            el = l.strip().split('|')
            rules[el[0]].append(el[1])
        else:
            curr = l.strip().split(',')
            tmp = []
            check = []
            bad = False
            i = 0
            while i < len(curr):
                page = curr[i]
                tmp.append(page)
                check = list(set(rules[page]) & set(tmp))
                if check:
                    iteration += 1
                    #print(f"X {curr} {page}:{check[0]}")
                    bad = True
                    tmp = []
                    j = curr.index(check[0])
                    curr[i] = check[0]
                    i = 0
                    curr[j] = page
                    #print(f"XN {curr} j:{j} page:{page}")
                else:
                    i += 1
            if bad:
                #print(f"{count2}")
                count2 += int(curr[len(curr)//2])
            else :
                count1 += int(curr[len(curr)//2])

    print(count1)
    print(count2)

