from stats import *
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        letterbox = char_counter(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_counter(sys.argv[1])} total words")
        print("--------- Character Count -------")
        for i in range (0, len(letterbox)):
            helper = letterbox[i]
            if helper["char"] == " ":
                print(f'spaces: {helper["num"]}')
            elif helper["char"] == "\n":
                continue
            else:
                print(f'{helper["char"]}: {helper["num"]}')
        print("============= END ===============")
main()