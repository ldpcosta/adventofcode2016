import hashlib
import re

global memory
memory = dict()


def make_hash(toHash):
    md5 = hashlib.md5()
    md5.update(toHash)
    return md5.hexdigest()


def stretched_hash(toHash):
    h = make_hash(toHash)
    for i in range(0,2016):
        md5 = hashlib.md5()
        md5.update(h)
        h = md5.hexdigest()
    return h

def possible_solution(hashedString):
    rx = re.compile(r'(.)\1\1')
    found = rx.search(hashedString)
    if found:
        index = found.start()
        return hashedString[index]
    else:
        return False


def is_solution(hashedString):
    for key in sorted(memory.keys()):
        rxRule = memory[key] * 5
        rx = re.compile(rxRule)
        found = rx.search(hashedString)
        if found:
            return key
    return None


def main(salt):
    solutions = []
    garbage = [-1]
    i = 0
    while len(solutions) < 64:

        if garbage[0] < i - 1000:
            memory.pop(garbage[0], None)
            garbage.remove(garbage[0])
        toHash = salt + str(i)
        #hashedString = make_hash(toHash)
        hashedString = stretched_hash(toHash)
        if len(memory) > 0:
            sol = is_solution(hashedString)
            if sol:
                memory.pop(sol, None)
                garbage.remove(sol)
                solutions += [sol]
                continue

        char = possible_solution(hashedString)
        if char:
            memory[i] = char
            garbage += [i]

        i += 1
    return max(solutions)


if __name__ == "__main__":
    print main("zpqevtbw")