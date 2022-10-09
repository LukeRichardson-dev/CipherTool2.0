from dataclasses import dataclass
from typing import Callable
from typing_extensions import Self

from crypt_context import CryptCtx

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

    

