DEFAULT = [chr(i) for i in range(65, 91)]


def palyfair_transform(aidx, bidx, offset):
    ay, ax, by, bx = aidx // 5, aidx % 5, bidx // 5, bidx % 5
    
    if ax == bx:
        return ax, (ay + offset) % 5, bx, (by + offset) % 5
    if ay == by:
        return (ax + offset) % 5, ay, (bx + offset) % 5, by
    
    return bx, ay, ax, by


def forward(plaintext, key):

    monke = [key[i::5] for i in range(5)]
    prepped = prepare(plaintext)
    
    new = ''
    for a, b in zip(prepped[::2], prepped[1::2]):

        aidx, bidx = key.index(a), key.index(b)
        nax, nay, nbx, nby = palyfair_transform(aidx, bidx, 1)
        new += monke[nax][nay] + monke[nbx][nby]

    return new

def prepare(plaintext):
    plaintext = ''.join((a if a.upper() != 'J' else 'I').upper() if str(a).isalpha() else '' for a in plaintext)
    plaintext += 'Z' * (len(plaintext) % 2)
    plaintext = ''.join((a + b if a != b else f'{a}X{b}X' for a, b in zip(plaintext[::2], plaintext[1::2])))
    return plaintext

def keyword_to_key(keyword):

    alpha = set(DEFAULT).difference({'J'})
    key = [i for i in keyword]
    alpha.difference_update(key)
    return key + sorted(list(alpha))

def backward(ciphertext, key):

    monke = [key[i::5] for i in range(5)]
    
    new = ''
    for a, b in zip(ciphertext[::2], ciphertext[1::2]):

        aidx, bidx = key.index(a), key.index(b)
        ay, ax, by, bx = aidx // 5, aidx % 5, bidx // 5, bidx % 5
        
        if ax == bx:
            nax, nay, nbx, nby = ax, (ay - 1) % 5, bx, (by - 1) % 5
        elif ay == by:
            nax, nay, nbx, nby = (ax - 1) % 5, ay, (bx - 1) % 5, by
        else:
            nax, nay, nbx, nby = bx, ay, ax, by

        new += monke[nax][nay] + monke[nbx][nby]

    return new

def digraph(text):
    digraphs = {}
    for a, b in zip(text[::2], text[1::2]):

        ab = a + b
        v = digraphs.get(ab, 0)
        digraphs[ab] = v + 1

    return digraphs


if __name__ == '__main__':

    key = keyword_to_key('MONARCHY')

    EXAMPLE = 'instruments'
    res = forward(EXAMPLE, key)
    print(res)

    assert res == 'GATLMZCLRQTX'
    dec = backward(res, key)
    print(dec)

