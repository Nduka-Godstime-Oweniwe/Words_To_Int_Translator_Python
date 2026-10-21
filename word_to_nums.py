

import validate

def words_to_nums(words):
    if not validate.valid_words(words):
        return "Invalid Words"