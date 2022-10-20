from text import Text
from typing_extensions import Self

STANDARD_FREQUENCIES = [8.4966,2.0720,4.5388,3.3844,11.1607,1.8121,2.4705,3.0034,7.5448,0.1965,1.1016,5.4893,3.0129,6.6544,7.1635,3.1671,0.1962,7.5809,5.7351,6.9509,3.6308,1.0074,1.2899,0.2902,1.7779,0.2722]


class FrequencyCtx:

    def __init__(self, frequencies=None, *, m=26) -> None:
        
        self.frequencies = frequencies
        if frequencies is None:
            self.frequencies = [0] * m

    @property
    def percentage(self):

        total = sum(self.frequencies)
        if total == 0: return [100 / len(self.frequencies)] * len(self.frequencies)
        return [100 * (i / total) for i in self.frequencies]

    def run(self, arg, transformer):

        return transformer(self, arg)

    @staticmethod
    def count(ctx: Self, text: Text):
        n_freqs = ctx.frequencies.copy()
        
        for i in text.glyphs:
            n_freqs[i] += 1

        return FrequencyCtx(n_freqs, m=len(n_freqs))

    def compare_to_distribution(self, distribution: list[float]):

        return sum([abs(a - b) for a, b in zip(distribution, self.percentage)])

    def predict_letter(self, letter: int, distribution: list[int]):

        target = distribution[letter]
        distances = [*enumerate((abs(target - l) for l in self.percentage))]
        
        distances.sort(key=lambda a: a[1])

        return [i for i, _ in distances], [i for _, i in distances]
