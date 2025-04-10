from stats import count_letters, count_text_words, stats_report


def main():
    frank = "books/frankenstein.txt"
    book = get_book_text(frank)
    words = count_text_words(book)
    letters = count_letters(book)
    stats_report(words, letters)


def get_book_text(path):
    with open(path, "r") as fl:
        book = fl.read()
    return book


if __name__ == "__main__":
    main()
