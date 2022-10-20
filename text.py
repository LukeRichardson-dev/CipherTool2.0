class Text:

    def __init__(self, text):

        self.text = text

    @property
    def mask(self):
        return "".join((
            (
                ('A' if l.isupper() else 'a')
                if l.isalpha() else l
            ) 
            for l in self.text
        ))

    # TODO: Make not shit
    def __mul__(self, other: list[int]):
        new = ""
        text_index = 0

        mask = self.mask

        while len(new) < len(mask):

            msk = mask[len(new)]

            if msk in ['a', 'A']:

                char = Text.decode(other[text_index])

                if msk == 'a':

                    char = char.lower()

                msk = char                
                text_index += 1

            new += msk

        return new

    @property
    def words(self):

        words = self.text.split(" ")

        for idx, word in enumerate(words):

            words[idx] = "".join(filter(lambda x: x.isalpha(), word))

        return words

    @property
    def letters(self):

        for i in self.text:

            if i.isalpha():
                yield i

    @property
    def glyphs(self):

        for letter in self.letters:

            yield Text.encode(letter)

    @staticmethod
    def encode(char, *, m=26):

        return (char.upper().encode()[0] - 65) % m 

    @staticmethod
    def decode(rep):

        return chr(rep + 65)

