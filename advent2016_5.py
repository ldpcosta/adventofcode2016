import hashlib
import sys

def find_char(inp, i=0):
    c = 0
    while c != 8:
        testinp = (inp + str(i))

        m = hashlib.md5()
        m.update(testinp)
        evalhash = m.hexdigest()

        if evalhash[:5] == "0"*5:
            sys.stdout.write(evalhash[5])
            c += 1

        i += 1

def find_outoforder(inp):
    passw = [None]*8

    i = 0
    while None in passw:
        testinp = (inp + str(i))

        m = hashlib.md5()
        m.update(testinp)
        evalhash = m.hexdigest()

        if evalhash[:5] == "0"*5 and 0 <= int(evalhash[5], 16) <= 7:
            if passw[int(evalhash[5])] == None:

                passw[int(evalhash[5])] = evalhash[6]


        i += 1

    return passw

if __name__ == "__main__":
    inp = "ugkcyxxp"
    find_char(inp,0)
    print "".join(find_outoforder(inp))