from stats import get_number_of_words,  get_number_of_chars
def get_book_text(path_to_book):
    with open(path_to_book , encoding="utf-8") as f:
        book_text = f.read()
    return book_text


def main():
    book = get_book_text("books/frankenstein.txt")
    # print(f"{get_number_of_words(book)} words found in the document")
    print(get_number_of_chars(book))
    
if __name__  == "__main__":
    main()