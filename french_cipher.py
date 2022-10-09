from dataclasses import dataclass
from typing_extensions import Self

from affine import Affine
from crypt_context import CryptCtx


# vinigere?
# viginere?
# vinegar?
class FrenchCipher:

    def __init__(self, keys: list[int], *, m=26):

        self.m = m
        self.keys = [Affine(1, i, m) for i in keys]

    @staticmethod
    def encrypt(ctx: CryptCtx, vin: Self):

        index = (len(ctx.decrypted) - 1) % len(vin.keys)
        aff: Affine = vin.keys[index]
        
        return Affine.encrypt(ctx, aff)

    @staticmethod
    def decrypt(ctx: CryptCtx, vin: Self):

        index = (len(ctx.decrypted)) % len(vin.keys)
        aff: Affine = vin.keys[index]
        
        return Affine.decrypt(ctx, aff)

    