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

    # def sort_dict(dictionary):
    #     return sorted(dictionary.items(), key=lambda x:x[1], reverse=True)

def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char":char, "num":count})
            
    char_list.sort(key= lambda x: x["num"], reverse=True)
    return char_list