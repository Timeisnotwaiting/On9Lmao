from config import COMMAND_HANDLER as hl, on9_id
from english_words import english_words_set as ews
from hlpl_english_words import english_words

case=['adjective','adverb','noun-singular','noun-plural','verb','article']

alpha_words = []

def load_words():
    global alpha_words
    if len(alpha_words) > 1300000:
        return
    for mad in case:
        for red in english_words.get(mad):
            for dy in red:
                alpha_words.append(dy)
    for jerk in ews:
        alpha_words.append(jerk)

def get_classic_word(letter, length, BIN):
    for x in alpha_words:
        if x.lower() in BIN:
            continue
        if x[0].lower() == letter.lower():
            if len(x) >= length:
                BIN.append(x.lower())
                return x

load_words()
