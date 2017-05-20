class Disk():
    def __init__(self, startpos, size):
        self.pos = startpos
        self.size = size

    def incr(self):
        self.pos += 1
        if self.pos == self.size:
            self.pos = 0


def parser(inp):
    discs = []
    for disc in inp:
        disc = disc.split(" ")

        size = int(disc[3])
        startPos = int(disc[-1][0])
        discs += [Disk(startPos, size)]
    return discs


def pos_to_disk_pos(position, disksize):
    while position >= disksize:
        position -= disksize
    return position


def main(inp):
    discs = parser(inp)
    t = 0

    while True:
        mem = [None]*len(discs)
        for i, d in enumerate(discs):
            if pos_to_disk_pos((d.pos+i), d.size) == 0:
                mem[i] = True
            else: mem[i] = False
        if reduce(lambda x,y: x and y, mem):
            return t-1
        t += 1
        for d in discs:
            d.incr()


if __name__ == "__main__":
    inp = """Disc #1 has 7 positions; at time=0, it is at position 0.
Disc #2 has 13 positions; at time=0, it is at position 0.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 2.
Disc #5 has 17 positions; at time=0, it is at position 0.
Disc #6 has 19 positions; at time=0, it is at position 7.
Disc #7 has 11 positions; at time=0, it is at position 0.""".split("\n")
    print main(inp)
