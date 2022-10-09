from dataclasses import dataclass


@dataclass
class CryptCtx:

    encrypted: list[int]
    decrypted: list[int]
    
    @property
    def length(self):

        return len(self.decrypted) + len(self.encrypted)

    @property
    def decryption(self):

        return len(self.decrypted) / self.length

    @property
    def encryption(self):

        return len(self.decrypted) / self.length

    def run_once(self, arg, transform):

        new_ctx = transform(self, arg)
        
        return new_ctx

    def run_full(self, arg, transform):

        ctx = transform(self, arg)

        while ctx.encryption not in [0.0, 1.0]:

            ctx = transform(ctx, arg)

        return ctx

    def encrypt(self, transform, *, block_size=1):
        enciphered_glyph = transform(self.decrypted[-block_size])

        return CryptCtx (
            [enciphered_glyph] + self.encrypted,
            self.decrypted[:-block_size],
        )

    def decrypt(self, transform):
        deciphered_glyph = transform(self.encrypted[0])

        return CryptCtx(
            self.encrypted[1:],
            self.decrypted + [deciphered_glyph]
        )

    

