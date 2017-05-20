import numpy as np

size = (6,50)
screen = np.chararray(size)
screen[:] = "."

def rect(a,b, screen = screen):
    screen[:b,:a] = "#"
    return screen


def rotate_col(col, n, size=size):
    newcol = screen[col]

    p = True
    if n < 0:
        p = False

    n = abs(n)
    while abs(n) > size[1]:
        n -= size[1]
    n_ = size[1] - n

    if p:
        a = newcol[:-n]
        b = newcol[n_:]
    else:
        a = newcol[:-n_]
        b = newcol[n:]

    newcol = np.append(b,a)
    screen[col, :] = newcol[:]
    return screen


def rotate_row(row, n, size=size):
    newrow = screen[:, row]

    p = True
    if n < 0:
        p = False

    n = abs(n)
    while abs(n) > size[0]:
        n -= size[0]
    n_ = size[0] - n

    if p:
        a = newrow[:-n]
        b = newrow[n_:]
    else:
        a = newrow[:-n_]
        b = newrow[n:]

    newrow = np.append(b,a)
    screen[:, row] = newrow[:]
    return screen


def parse_input(elem):
    elem = elem.split(" ")
    if "rect" in elem:
        a, b = int(elem[1].split("x")[0]), int(elem[1].split("x")[1])
        return rect(a,b)
    elif "column" in elem:
        row, n = int(elem[2].split("=")[1]), int(elem[4])
        return rotate_row(row, n)
    elif "row" in elem:
        col, n = int(elem[2].split("=")[1]), int(elem[4])
        return rotate_col(col, n)


if __name__ == "__main__":

    with open("advent2016_8_inp", "r") as f:
        inp = "".join(f.readlines()).split("\n")

    for elem in inp:
        parse_input(elem)

    counter = 0
    for elem in screen:
        unique, counts = np.unique(elem, return_counts=True)
        add = dict(zip(unique,counts)).get("#")
        if add != None:
            counter += add
    print counter, "\n"

    prevn, n = 0, 5
    while n<=50:
        print screen[:6,prevn:n], "\n"
        prevn, n = n, n+5