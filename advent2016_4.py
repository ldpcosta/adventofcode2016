import string


def parse_name(inp):
    return "".join(inp[:-10].split("-"))


def parse_checksum(inp):
    return [i for i in inp[-6:-1]]


def parse_ID(inp):
    return int(inp[-10:-7])


def most_common_characters(room):

    def different_characters(room):
        st = set()
        for char in room:
            st.add(char)
        return st

    def sort_characters(char_count):
        key = lambda x: (x[1] * -1, x[0])
        return sorted(char_count, key=key)

    char_count = dict()

    for char in different_characters(room):
        char_count[char] = room.count(char)

    return [i for i, j in sort_characters(char_count.items())][:5]


def compare_inp(inp):
    room = parse_name(inp)
    checksum =  parse_checksum(inp)
    if most_common_characters(room) == checksum:
        return parse_ID(inp)
    else:
        return 0

def solve_cipher(inp):
    room = parse_name(inp)
    id = parse_ID(inp)

    dic = string.lowercase
    max_val = ord("a") + len(dic)

    st = ""

    for char in room:
        val = ord(char) + id
        while val >= max_val:
            val -= len(dic)

        st += chr(val)

    return st

if __name__ == "__main__":
    with open("advent2016_4_inp.txt", "r") as file:
        inp = "".join(file.readlines())

    ls = []
    for elem in inp.split("\n"):
        ls += [compare_inp(elem)] # Ex.1

        if "north" in solve_cipher(elem): #Ex.2
            print solve_cipher(elem), parse_ID(elem)

    print sum(ls)

