import sys

arg_input = sys.argv[1]

def part1(f):
    safeCount = 0
    for l in f:
        report = list(map(int, l.split(" ")))

        # Part 1
        isIncrease = report[1] > report[0] and report[1] - report[0] <= 3
        isDecrease = report[0] > report[1] and report[0] - report[1] <= 3
        safe = True
        if isDecrease or isIncrease:
            for i in range(2, len(report)):
                if isIncrease and report[i] > report[i-1] and report[i] - report[i-1] <= 3:
                    continue
                elif isDecrease and report[i-1] > report[i] and report[i-1] - report[i] <= 3:
                    continue
                safe = False
                break
            if safe:
                print(f"safe {report}")
                safeCount += 1
    print(f"safe {safeCount}")

def part2(f):
    safeCount = 0
    for l in f:
        report = list(map(int, l.split(" ")))

        for j in range(-1, len(report)):
            copy = report.copy()
            if j >= 0:
                copy.pop(j)
            safe = testReport(copy)
            if safe:
                break

        if safe:
            print(f"safe {report} j:{j}")
            safeCount += 1
        else:
            print(f"unsafe {report} j:{j}")
    print(f"safeCount {safeCount}")


def testReport(report):
        isIncrease = report[1] > report[0] and report[1] - report[0] <= 3
        isDecrease = report[0] > report[1] and report[0] - report[1] <= 3
        safe = True
        if isDecrease or isIncrease:
            for i in range(2, len(report)):
                if isIncrease and report[i] > report[i-1] and report[i] - report[i-1] <= 3:
                    continue
                elif isDecrease and report[i-1] > report[i] and report[i-1] - report[i] <= 3:
                    continue
                safe = False
                break
        else:
            safe = False
        return safe


with open(arg_input, 'r') as f:
    #part1(f)
    part2(f)