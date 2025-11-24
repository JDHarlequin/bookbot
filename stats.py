def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_counter():
    book = get_book_text("books/frankenstein.txt")
    word_count = len(book.split())
    return word_count

def char_counter():
    book = get_book_text("books/frankenstein.txt")
    book = book.lower()
    print(book)