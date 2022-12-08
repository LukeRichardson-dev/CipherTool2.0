NORMALISATION_COEFFICIENT_OF_HIS_MAJESTIES_ENGLISH_LEXICON = 26

def index_of_conicidence(text: str):
    text = text.upper()
    N = len(text)
    total = 0
    for char in (chr(j + 65) for j in range(26)):
        f = text.count(char)
        total += (f * (f - 1)) / (N * (N - 1))

    return total * NORMALISATION_COEFFICIENT_OF_HIS_MAJESTIES_ENGLISH_LEXICON