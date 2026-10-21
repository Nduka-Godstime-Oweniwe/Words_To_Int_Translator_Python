import validate

def nums_to_words(num):
    if not validate.valid_num(num):
        return "Invalid Number"