
class Wordlist:

    def __init__(
        self, 
        path='./wordlists/20k.txt', *,
        ordered = True,
        _operations = [],
        _filters = [],
    ):

        self.path = path
        self.ordered = ordered
        self._operations = _operations
        self._filters = _filters

    def get_lines(
        self, *,
        limit = None,
    ):

        if (limit is None):
            def step(_): return False
        else:
            def step(line_number): return line_number >= limit

        def compound_filter(line):

            return not any(map(lambda fn: fn(line), self._filters))

        with open(self.path) as wlst:

            for line_no, line in enumerate(filter(compound_filter, wlst)):
                
                if step(line_no): break

                line = line.rstrip()

                for op in self._operations:
                    line = op(line)

                yield line

    def add_operations(self, *operations):

        return Wordlist(
            self.path,
            ordered=self.ordered,
            _operations = self._operations.copy() + operations,
            _filters = self._filters.copy(),
        )

    def add_filters(self, *filters):

        return Wordlist(
            self.path,
            ordered=self.ordered,
            _operations = self._operations.copy(),
            _filters = self._filters.copy() + filters,
        )
