def operation(inp):
    a = inp
    b = a[::-1]

    b_ = ""
    for ch in b:
        if ch == "1":
            b_ += "0"
        else:
            b_ += "1"

    b = b_
    return a+"0"+b


def fill_disk(inp, diskLength):
    while len(inp) < diskLength:
        inp = operation(inp)

    if len(inp) > diskLength:
        inp = inp[:diskLength+1]

    return inp


def generate_checksum(inp):

    def new_checksum(inp):

        testPairs = zip(inp[::2], inp[1::2])

        checksum = ""

        for elem in testPairs:
            if elem[0] == elem[1]:
                checksum += "1"
            else:
                checksum += "0"

        return checksum

    checksum = new_checksum(inp)
    while len(checksum)%2 == 0:
        checksum = new_checksum(checksum)
    return checksum

if __name__ == "__main__":
    inp = "01111010110010011"
    # diskLength = 272
    diskLength = 35651584

    print generate_checksum(fill_disk(inp, diskLength))


