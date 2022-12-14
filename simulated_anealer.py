from qgram import score
from playfair import backward, keyword_to_key
from math import exp
from random import random, randrange
from hill_climbing import TEST, score_by_ic

TEMP = 20
STEP = 0.2
MAX_COUNT = 10_000

def show_key(key):

    for i in range(5):
        print(''.join(key[i::5]))

def run(text):

    bk = [i for i in 'ABCDEFGHIKLMNOPQRSTUVWXYZ']
    
    while True:

        bs, bk = crackPlayfair(text, bk)
        print(bs)
        show_key(bk)

def crackPlayfair(text, key):
    bestKey = key.copy()
    maxKey = key.copy()

    bestScore = scoreKey(text, key)
    topScore = bestScore
    print(topScore)

    T = TEMP
    while T > 0:

        for count in range(MAX_COUNT):

            testKey = modifyKey(maxKey)
            score = scoreKey(text, testKey)
            dF = score - topScore
            if dF >= 0:
                topScore = score
                maxKey = testKey

            elif T > 0:

                probability = exp(dF/T)
                if probability > random():
                    topScore = score
                    maxKey = testKey

            if topScore > bestScore:
                bestScore = topScore
                bestKey = maxKey.copy()

            T -= STEP

    return bestScore, bestKey
            

def scoreKey(text, key):

    return score(backward(text, key))

def modifyKey(key):

    perm = randrange(0, 20)

    if perm == 0:
        nkey = swap_rows(key)
    elif perm == 1:
        nkey = swap_cols(key)
    elif perm == 2:
        nkey = key[::-1]
    elif perm == 3:
        nkey = [*key[4::5], *key[3::5], *key[2::5], *key[1::5], *key[::5]]
    elif perm == 3:
        nkey = [*key[25:20], *key[20:15], *key[15:10], *key[10:5], *key[5:]]
    else:
        nkey = swap_chars(key)

    return nkey

def swap_chars(key):

    nkey = key.copy()
    sw1, sw2 = randrange(0, 25), randrange(0, 25)
    t = nkey[sw1]
    nkey[sw1] = nkey[sw2]
    nkey[sw2] = t

    return nkey

def swap_rows(key):
    
    r1 = randrange(0, 5)
    r2 = randrange(0, 5)

    row1 = key[r1*5:(r1+1)*5]
    row2 = key[r2*5:(r2+1)*5]

    nkey = []
    for r in range(5):

        if r == r1:
            nkey.extend(row2)

        elif r == r2:
            nkey.extend(row1)

        else:
            nkey.extend(key[r*5:(r+1)*5])

    return nkey


def swap_cols(key):
    
    c1 = randrange(0, 5)
    c2 = randrange(0, 5)

    col1 = key[c1::5]
    col2 = key[c2::5]

    nkey = []
    for c in range(5):

        if c == c1:
            nkey.extend(col2)

        elif c == c2:
            nkey.extend(col1)

        else:
            nkey.extend(key[c::5])

    return nkey

if __name__ == '__main__':

    run(TEST)