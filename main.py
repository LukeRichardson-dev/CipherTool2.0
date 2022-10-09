from affine import Affine
from crypt_context import CryptCtx
from french_cipher import FrenchCipher
from text import Text


if __name__ == '__main__':

    text = Text("Hello, World!")
    serialised = [*text.glyphs]

    vin_key = [*Text("xftjhjtyd").glyphs]
    vin = FrenchCipher(vin_key)

    ctx = CryptCtx([], serialised)

    nctx = ctx.run_full(vin, FrenchCipher.encrypt)
    print(text * nctx.encrypted)

    nctx = nctx.run_full(vin, FrenchCipher.decrypt)
    print(text * nctx.decrypted)