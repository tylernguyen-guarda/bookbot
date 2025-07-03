def get_number_of_words(text):
    return len(text.split())

def get_number_of_chars(text):
    char_dict = {}
    for letter in text:
        if char_dict.get(letter.lower()) is None:
            char_dict.setdefault(letter.lower(),1)
        else:
            char_dict[letter.lower()] += 1
    return char_dict