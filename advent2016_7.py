import re


def search_squares(st):
    ruleGood = re.findall(r"""(?:^|\])([^\[]+)(?:\[|$)""", st)
    ruleBad = re.findall(r"\[([^\]]+)\]", st)

    if type(ruleBad) == str:
        ruleBad = [ruleBad]

    return ruleGood, ruleBad


def has_tls(st):

    def is_palindrome(st):
        if st[:2] == st[-1:1:-1]  and st[0] != st[1]:
            return True
        return False

    for ind in xrange(len(st) - 3):
        subst = st[ind:ind + 4]

        if is_palindrome(subst):
            return True
    return False


def is_tls(inp):
    squares = search_squares(inp)
    good = [has_tls(st) for st in squares[0]]
    bad = [has_tls(st) for st in squares[1]]
    if len(good) < 2 and len(bad) < 1:
        return False
    if True in good and True not in bad:
        return True
    return False



def has_ssl(st, hyper = False):
    def is_palindrome(st):
        if st[0] == st[-1] and st[0] != st[1]:

            if hyper:
                return (st[0], st[1])
            else:
                return (st[1], st[0])
        return []

    sublist = []
    for ind in xrange(len(st)-1):
        subst = st[ind:ind + 3]
        sub = is_palindrome(subst)
        if sub != []:
            sublist += [sub]


    return sublist


def is_ssl(inp):
    squares = search_squares(inp)

    out = []
    for st in squares[0]:
        ssl_st = has_ssl(st)
        if ssl_st:
            out.extend(ssl_st)

    ins = []
    for st in squares[1]:
        ssl_st = has_ssl(st, True)
        if ssl_st:
            ins.extend(ssl_st)

    for elem in ins:
        if elem in out:
            return True
    return False


if __name__ == "__main__":
    with open("advent2016_7_inp", "r") as f:
        inp = "".join(f.readlines()).split("\n")

    print "TLS", sum([is_tls(i) for i in inp])
    print "SSL", sum([is_ssl(i) for i in inp])
