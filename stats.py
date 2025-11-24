def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_counter():
    book = get_book_text("books/frankenstein.txt")
    word_count = len(book.split())
    return word_count

def char_counter():
    ccount = {}
    book = get_book_text("books/frankenstein.txt")
    book = book.lower()
    for letter in range(0, len(book)):
        if book[letter] not in ccount:
            ccount[book[letter]] = 1
        else:
            ccount[book[letter]] += 1
    print(ccount)