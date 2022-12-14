from config import COMMAND_HANDLER as hl, on9_id
from english_words import english_words_set as ews
from hlpl_english_words import english_words
import time

startTime = time.time()

AM = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

case=['adjective','adverb','noun-singular','noun-plural','verb','article']

A_M = []
N_Z = []

def load_words():
    global A_M, N_Z
    if len(A_M + N_Z) > 1300000:
        return
    for mad in case:
        for red in english_words.get(mad):
            for dy in red:
                if dy[0].lower() in AM:
                    A_M.append(dy)
                else:
                    N_Z.append(dy)
    for jerk in ews:
        if jerk[0].lower() in AM:
            A_M.append(jerk)
        else:
            N_Z.append(jerk)

def get_classic_word(letter, length, BIN):
    if letter.lower() in AM:
        for x in A_M:
            if x.lower() in BIN:
                continue
            if x[0].lower() == letter.lower():
                if len(x) >= length:
                    A_M.remove(x)
                    BIN.append(x.lower())
                    return x
    else:
        for x in N_Z:
            if x.lower() in BIN:
                continue
            if x[0].lower() == letter.lower():
                if len(x) >= length:
                    N_Z.remove(x)
                    BIN.append(x.lower())
                    return x

    

load_words()
