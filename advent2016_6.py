import string

def parse_columns(inp):
    inp = inp.split("\n")
    ls = []
    for i in range(len(inp[0])):
        s = ''
        for elem in inp:
            s += elem[i]

        ls += [s]

    return ls


def most_common(ls, rev=True):

    def different_characters(elem):
        st = set()
        for char in elem:
            st.add(char)
        return st

    mcom = []
    for elem in ls:
        chars = different_characters(elem)
        values = []
        for c in chars:
            values += [(elem.count(c), c)]

        mcom += [sorted(values, reverse=rev)[0][1]]

    return "".join(mcom)

if __name__ == "__main__":
    with open("advent2016_6_inp", "r") as file:
        inp = "".join(file.readlines())

    print most_common(parse_columns(inp))
    print most_common(parse_columns(inp), rev=False)
