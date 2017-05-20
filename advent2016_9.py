def parse_text(inp):

    def parse_marker(marker):
        marker = marker[1:-1].split("x")
        return [int(i) for i in marker]

    st = ""
    subst = ""
    marker = ""
    isMarker = False

    skip = 0
    repeat = 0

    for c in inp:
        if skip == 0 and subst != "" and repeat != 0:

            if "(" in subst:
                print subst
                subst = parse_text(subst)

            st += subst * repeat
            subst = ""
            repeat = 0
            if c != "(":  # if is not a nested marker
                st += c
                continue

        if skip > 0:
            subst += c
            skip -= 1
            continue

        if not isMarker and c != "(":
            st += c
        else:
            marker += c
            isMarker = True
            if c == ")":

                isMarker = False
                skip, repeat = parse_marker(marker)
                print marker, skip, repeat, subst
                marker = ""

    st += subst * repeat
    return st


if __name__ == "__main__":
    with open("advent2016_9_inp", "r") as f:
        inp = f.read()[:-3]

    print parse_text("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")




