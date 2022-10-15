from text import Text
from typing_extensions import Self

class FrequencyCtx:

    def __init__(self, frequencies=None, *, m=26) -> None:
        
        self.frequencies = frequencies
        if frequencies is None:
            frequencies = [0] * m

    @property
    def percentage(self):

        total = sum(self.frequencies)
        if total == 0: return [0] * len(self.frequencies)

    def run(self, arg, transformer):

        return transformer(self, arg)

    @staticmethod
    def count(ctx: Self, text: Text):
        n_freqs = ctx.frequencies.copy()
        
        for i in text.glyphs:
            n_freqs[i] += 1

        return FrequencyCtx(n_freqs, m=len(n_freqs))
