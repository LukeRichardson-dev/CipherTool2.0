from affine import Affine, solve_affine, solve_ceasar
from analysis import STANDARD_FREQUENCIES, FrequencyCtx
from crypt_context import CryptCtx
from french_cipher import FrenchCipher
from samples import SIMPLE_CEASAR, WEEK_ONE, WEEK_ONE_B
from text import Text
from wordlists import Wordlist, score_by_wordlist


def main():

    # text = Text("Hello, World!")
    text = SIMPLE_CEASAR
    serialised = [*text.glyphs]

    vin_key = [*Text("h").glyphs]
    vin = FrenchCipher(vin_key)

    ctx = CryptCtx(serialised, [])

    # ctx = ctx.run_full(vin, FrenchCipher.encrypt)
    # print(text * ctx.encrypted)

    ctx = ctx.run_full(vin, FrenchCipher.decrypt)
    print(text * ctx.decrypted)


if __name__ == '__main__':

    wl = Wordlist()
    words = [*wl.get_lines(limit=100000)]
    # dec = solve_affine(SIMPLE_CEASAR, lambda x: score_by_wordlist(x, words))
    dec = solve_ceasar(WEEK_ONE_B, lambda x: score_by_wordlist(x, words))
    for i in dec:
        print(i)
        if input() == "q":
            break