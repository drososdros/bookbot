import sys

from stats import count_letters, count_text_words, stats_report


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(args[1])
    words = count_text_words(book)
    letters = count_letters(book)
    stats_report(words, letters)


def get_book_text(path):
    with open(path, "r") as fl:
        book = fl.read()
    return book


if __name__ == "__main__":
    main()
