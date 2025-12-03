from stats import count_word, count_char, get_char_dics
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def sort_on(item):
    return item["num"]


def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")

        txt = get_book_text(sys.argv[1])
        print(f"Found {count_word(txt)} total words")

        print("--------- Character Count -------")
        count_char_dic = count_char(txt)
        sorted = get_char_dics(count_char_dic)
        sorted.sort(reverse=True, key=sort_on)
        for c in sorted:
            print(f"{c["char"]}: {c["num"]}")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
