from dataclasses import dataclass
from typing_extensions import Self
from analysis import STANDARD_FREQUENCIES, FrequencyCtx
from crypt_context import CryptCtx
from text import Text

def inv_mod(a, m):

    for b in range(m):

        res = a * b % m
        if res == 1:
            return b

@dataclass
class Affine:

    a: int
    b: int
    m: int

    def check(self):

        return self.a // self.m != self.a / self.m and \
            self.m // self.a != self.m / self.a

    @staticmethod
    def decrypt(ctx: CryptCtx, aff: Self):

        decipher = lambda x: (inv_mod(aff.a, aff.m) * (x - aff.b)) % aff.m
        return ctx.decrypt(decipher)
    
    @staticmethod
    def encrypt(ctx: CryptCtx, aff: Self):

        encipher = lambda x: (aff.a * x + aff.b) % aff.m
        return ctx.encrypt(encipher)

def solve_ceasar(text, scorer):

    freq = FrequencyCtx()
    freq = freq.run(text, FrequencyCtx.count)

    scores = { i: 0 for i in range(26) }
    for i in range(26):
        ls, fs = freq.predict_letter(i, STANDARD_FREQUENCIES)
        for l, f in zip(ls, fs):
            scores[(l - i) % 26] += f

    scorepairs = [*map(lambda x: (x[0], x[1]), scores.items())]
    scorepairs.sort(key=lambda x: x[1])

    ctx = CryptCtx([*text.glyphs], [])
    for i, _ in scorepairs:
        
        aff = Affine(1, i, 26)
        nctx = ctx.run_full(aff, Affine.decrypt)
        
        dec = text * nctx.decrypted
        
        score = scorer(Text(dec))
        yield i, dec, score

def solve_affine(text, scorer):

    fctx = FrequencyCtx.count(FrequencyCtx(), text)
    a, b, _ = solve_a_b(fctx.frequencies)

    ctx = CryptCtx([*text.glyphs], [])
    aff = Affine(a, b, 26)
    ctx = ctx.run_full(aff, Affine.decrypt)
    
    return text * ctx.decrypted

def solve_a_b(_freqs):

    aim = STANDARD_FREQUENCIES.copy()
    freqs = _freqs.copy()

    ascore = (-1, -1, 1000) # TODO: make less unuseable
    for a in range(1, 26):
        if a / 2 == a // 2: continue
        if a / 13 == a // 13: continue

        shifted = shift_freq(freqs.copy(), a)
        score = (-1, 1000)

        for i in range(26):

            diff = [abs(aim[idx] - f) for idx, f in enumerate(shifted)]
            score = min(((25-i)%26, sum(diff)), score, key=lambda x: x[1])
            
            shifted = shifted[1:] + [shifted[0]]
        
        ascore = min((a, score[0], score[1]), ascore, key=lambda x: x[2])

    return ascore

def shift_freq(freq, a):

    mask = [(a * i) % 26 for i in range(26)]
    return [freq[i] for i in mask]