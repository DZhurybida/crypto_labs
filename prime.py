import math

ptab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def checkptab(trialdivbound):
    global ptab
    g = ptab[-1]
    while ptab[-1] < trialdivbound:
        g += 2
        h = math.ceil(math.sqrt(g))
        for p in ptab:
            if p > h:
                suc = 1
                break
            if (g % p) == 0:
                suc = 0
                break
        if suc == 0:
            continue
        ptab += [g]
    return


checkptab(2 ** 10)
