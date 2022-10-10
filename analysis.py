
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


