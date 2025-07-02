def get_number_of_words(text):
    return len(text.split())

def get_number_of_chars(text):
    char_dict = {}
    for letter in text:
        if char_dict.get(letter.lower()) is None:
            print(f"found letter '{letter.lower()}'")
            char_dict.setdefault(letter.lower(),"0")
    return char_dict
            