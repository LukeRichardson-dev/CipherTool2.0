from _qgrams import QGRAMS

def score(text):
    s = 0
    for a, b, c, d in zip(*(text[i::] for i in range(4))):

        oa, ob, oc, od = ord(a) - 65, ord(b) - 65, ord(c) - 65, ord(d) - 65
        s += QGRAMS[17576*oa + 676*ob + 26*oc + od]

    return s