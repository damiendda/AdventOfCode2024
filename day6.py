import sys
import copy

arg_input = sys.argv[1]


def score(world, x, y):
    if world[y][x] == 'X':
        return 0
    else:
        return 1

def print_world(world):
    for l in world:
        print("".join(l))

def test_loop_(worldBefore, iX, iY):
    end = False
    result = False
    first = True
    arrow = '^'
    x = iX
    y = iY
    issue = 0
    worldB = copy.deepcopy(worldBefore)
    while end == False and issue < 10000:
        issue += 1
        if arrow == '^':
            if first == False and iX == x and iY == y:
                result = True
                print("true")
                print_world(worldB)
                break
            elif worldB[y-1][x] == '#':
                arrow = '>'
                worldB[y][x] = '+'
            else:
                worldB[y][x] = '|'
                y -= 1
                if y == 0:
                    end = True
            first = False
        elif arrow == '>':
            if worldB[y][x+1] == '#':
                arrow = 'v'
                worldB[y][x] = '+'
            else:
                worldB[y][x] = '-'
                x += 1
                if x == len(worldB[0])-1:
                    end = True
        elif arrow == 'v':
            if y+1 >= len(worldB)-1:
                end = True
            elif worldB[y+1][x] == '#':
                arrow = '<'
                worldB[y][x] = '+'
            else:
                worldB[y][x] = '|'
                y += 1
                if y == len(worldB)-1:
                    end = True
        elif arrow == '<':
            if worldB[y][x-1] == '#':
                arrow = '^'
                worldB[y][x] = '+'
            else:
                worldB[y][x] = '-'
                x -= 1
                if x == 0:
                    end = True

    if issue == 10000:
        print("### ISSUE ###")
        #print_world(worldB)
        result = True
    if end == True:
        result == False
    return result


with open(arg_input, 'r') as f:
    world = []
    x = 0
    y = 0

    i = 0
    j = 0
    initX = 0
    initY = 0
    arrow = '^'
    for l in f.readlines():
        world.append(list(l))
        if '^' in l:
            x = l.index('^')
            y = j
        j+=1

    initX = x
    initY = y
    end = False
    count = 0
    while end == False:
        if arrow == '^':
            if world[y-1][x] == '#':
                arrow = '>'
            else:
                count += score(world, x, y)
                world[y][x] = 'X'
                y -= 1
                if y == 0:
                    end = True
        elif arrow == '>':
            if world[y][x+1] == '#':
                arrow = 'v'
            else:
                count += score(world, x, y)
                world[y][x] = 'X'
                x += 1
                if x == len(world[0])-1:
                    end = True
        elif arrow == 'v':
            if world[y+1][x] == '#':
                arrow = '<'
            else:
                count += score(world, x, y)
                world[y][x] = 'X'
                y += 1
                if y == len(world)-1:
                    end = True
        elif arrow == '<':
            if world[y][x-1] == '#':
                arrow = '^'
            else:
                count += score(world, x, y)
                world[y][x] = 'X'
                x -= 1
                if x == 0:
                    end = True
    count += 1
   
    world[y][x] = 'X'
    print_world(world)

    # part2
    i = 0
    obX = 0
    obY = 0
    count2 = 0
    for l in world:
        j = 0
        for e in l:
            if e == 'X':
                obX = i
                obY = j
                # Test
                world[initY][initX] = '^'
                world[obX][obY] = '#'
                print(f"T {i} {j}")
                loop = test_loop_(world, initX, initY)
                
                # Add count
                if loop == True:
                    count2 += 1
                # Continue
                world[obX][obY] = '.'
            j += 1

        i += 1

    print(count)
    print(count2)
