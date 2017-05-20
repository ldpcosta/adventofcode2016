
inp = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5".split(", ")

def getLocation(inp = inp):
    inp = list((c[0],int(c[1:])) for c in inp)
    direction = 0
    x, y = 0, 0
    memory = set()
    firstCross = None

    def getDirection(direction, turn):
        if turn == "R":
            direction += 1
            if direction == 4:
                direction = 0

        elif turn == "L":
            direction -= 1
            if direction == -1:
                direction = 3

        return direction


    def getFinalPos(direction, steps, x=x, y=y):
        if direction == 0:   # North
            x += elem[1]
        elif direction == 1: # East
            y += elem[1]
        elif direction == 2: # South
            x -= elem[1]
        else:                # West
            y -= elem[1]

        return x, y


    def move(direction, prevX, prevY, x, y):
        current_movement = []

        if direction == 0:
            for i in range(prevX + 1, x + 1):
                current_movement += [(i, y)]

        elif direction == 2:
            for i in range(prevX - 1, x - 1, -1):
                current_movement += [(i, y)]

        elif direction == 1:
            for i in range(prevY + 1, y + 1):
                current_movement += [(x, i)]
        else:
            for i in range(prevY - 1, y - 1, -1):
                current_movement += [(x, i)]

        return current_movement


    for elem in inp:
        direction = getDirection(direction, elem[0])

        prevX = x
        prevY = y

        x, y = getFinalPos(direction, elem[1], x, y)

        current_movement = move(direction, prevX, prevY, x, y)

        for a in current_movement:
            if a in memory and not firstCross != None:
                firstCross = abs(a[0]) + abs(a[1])

            else:
                memory.add(a)

    return firstCross, abs(x) + abs(y)


print "We end at distance: ", getLocation(inp)[1]
print "The first crossing is at distance: ", getLocation(inp)[0]