from stats import get_number_of_words,  get_number_of_chars, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_book):
    with open(path_to_book , encoding="utf-8") as f:
        book_text = f.read()
    return book_text


def main():
    #logic for sys args
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    
    book = get_book_text(path_to_book=path_to_book)
    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at books/frankenstein.txt...")
    # print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(book)} total words")
    
    # print("--------- Character Count -------")
    letters_dict = get_number_of_chars(book)
    
    sorted_list_of_char_count = chars_dict_to_sorted_list(letters_dict)    
    for char_info in sorted_list_of_char_count:
        char = char_info["char"]
        num = char_info["num"]
        print(f"{char}: {num}")
if __name__  == "__main__":
    main()