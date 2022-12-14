from qgram import score
from playfair import backward, keyword_to_key
from math import exp
from random import random, randrange
from hill_climbing import TEST, score_by_ic

TEMP = 20
STEP = 0.2
MAX_COUNT = 10_000

def run(text):

    bk = [i for i in 'ABCDEFGHIKLMNOPQRSTUVWXYZ']
    
    while True:

        bs, bk = crackPlayfair(text, bk)
        print(bs, bk)

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

    nkey = key.copy()
    sw1, sw2 = randrange(0, 25), randrange(0, 25)
    t = nkey[sw1]
    nkey[sw1] = nkey[sw2]
    nkey[sw2] = t

    return nkey


if __name__ == '__main__':

    run(TEST)