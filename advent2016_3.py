with open("advent2016_3_inp.txt", "r") as file:
    inp = "".join(file.readlines())


def parse_lines(inp):
    p = [entry.strip().split() for entry in inp.split("\n")]
    return p

def column_threes(inp):
    inp = parse_lines(inp)
    retInp = []
    for i in range(0,len(inp), 3):
        triangle1 = [inp[i][0], inp[i + 1][0], inp[i + 2][0]]
        triangle2 = [inp[i][1], inp[i + 1][1], inp[i + 2][1]]
        triangle3 = [inp[i][2], inp[i + 1][2], inp[i + 2][2]]
        retInp += [triangle1] + [triangle2] + [triangle3]
    return retInp

def is_triangle(x,y,z):
    ls = sorted([x,y,z])

    if ls[0] + ls[1] > ls[2]:
        return True
    return False


if __name__ == "__main__":

    triangles_lines = [is_triangle(int(x),int(y),int(z)) for x, y, z in parse_lines(inp)]
    print sum(triangles_lines)

    triangles_col = [is_triangle(int(x),int(y),int(z)) for x, y, z in column_threes(inp)]
    print sum(triangles_col)