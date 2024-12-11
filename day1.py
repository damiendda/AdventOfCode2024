import sys

arg_input = sys.argv[1]

def addElemIn(listData, elem):
    i = 0
    while i < len(listData) and listData[i] < elem:
        i+=1
    listData.insert(i, elem)

with open(arg_input, 'r') as f:
    a = []
    b = []
    for l in f:
        arr = l.split("   ")
        addElemIn(a, int(arr[0]))
        addElemIn(b, int(arr[1]))
    
    sumDistances = 0

    for i in range(0, len(a)):
        if b[i] > a[i]:
            sumDistances += b[i]-a[i]
        else:
            sumDistances += a[i]-b[i]
    
    print(f"size a:{len(a)} b:{len(b)} sum:{sumDistances}")

