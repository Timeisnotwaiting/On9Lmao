from config import COMMAND_HANDLER as hl, on9_id
from english_words import english_words_set as ews


def get_classic_word(letter, length, BIN):
    for x in ews:
        if x in BIN:
            continue
        if x[0].lower() == letter.lower():
            if len(x) == length:
                BIN.append(x.lower())
                return x
