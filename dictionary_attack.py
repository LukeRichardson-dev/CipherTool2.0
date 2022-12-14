from wordlists import Wordlist
from idxoc import index_of_conicidence
from playfair import backward, keyword_to_key
from random import shuffle

def keystream(wordlist):
    
    wl1 = list(wordlist.get_lines())
    shuffle(wl1)
    for i in wl1:
        for j in wordlist.get_lines():
            yield keyword_to_key(i + j)


def try_words(ws, text):

    for key in ws:

        res = backward(text, key)
        ic = index_of_conicidence(res)

        if ic > 1.6:
            print(key, ic)

if __name__ == '__main__':

    from hill_climbing import TEST

    try_words(keystream(Wordlist('./wordlists/wordlist.txt')), TEST)