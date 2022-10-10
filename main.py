from affine import Affine
from crypt_context import CryptCtx
from french_cipher import FrenchCipher
from samples import SIMPLE_CEASAR
from text import Text


if __name__ == '__main__':

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