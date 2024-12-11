import sys

arg_input = sys.argv[1]

with open(arg_input, 'r') as f:
    a = []
    b = {}
    for l in f:
        arr = l.split("   ")
        a.append(int(arr[0]))
        b[int(arr[1])] = b.setdefault(int(arr[1]), 0) + 1
    
    sumSimilarity = 0

    for i in range(0, len(a)):
        if a[i] in b:
            sumSimilarity += a[i] * b[a[i]]
    
    print(f"size a:{len(a)} b:{len(b)} sum:{sumSimilarity}")
