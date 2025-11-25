def sorter_helper(c):
    return c["num"]

def get_book_text(path):
    with open(path, encoding="utf-8-sig") as f:
        file_contents = f.read()
    return file_contents

def word_counter(path):
    book = get_book_text(path)
    word_count = len(book.split())
    return word_count

def char_counter(path):
    ccount = {}
    sorted_ccount = []
    book = get_book_text(path)
    book = book.lower()
    for letter in range(0, len(book)):
        if book[letter] not in ccount:
            ccount[book[letter]] = 1
        else:
            ccount[book[letter]] += 1
    for key in ccount:
        sorted_ccount.append({"char": key, "num": ccount[key]})
    sorted_ccount.sort(reverse=True, key=sorter_helper)
    return sorted_ccount