import re


def parse_inp(inp):

    def parse_marker(marker):
        marker = re.split(r"\(|\)|x", marker)
        mark2 = [int(i) for j, i in enumerate(marker) if i != "" and j <= 2]
        return mark2[0], mark2[1]

    count = 0
    isMarker = False
    marker = ""
    subst = ""
    skip = 0

    for c in inp:
        count += 1

        if c == "(":
            marker += c
            isMarker = True

        elif isMarker:
            marker += c

        if c == ")" and isMarker and subst != "":
            ## In case several markers are inside a substring.
            isMarker = False
            marker = ""

        if c == ")" and isMarker and subst == "":
            skip, repeat = parse_marker(marker)
            if subst == "":
                count -= len(marker)
            marker = ""
            isMarker = False
            continue

        if skip > 0:
            skip -= 1
            count -= 1
            subst += c

        if skip == 0 and subst != "":

            count += parse_inp(subst) * repeat
            subst = ""
            repeat = 0

    return count

if __name__ == "__main__":
    with open("advent2016_9_inp", "r") as f:
        inp = f.read()[:-3]
    print parse_inp(inp)
