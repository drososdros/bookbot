from stats import count_text_words


def main():
    frank = "books/frankenstein.txt"
    book = get_book_text(frank)
    print(f"{count_text_words(book)} words found in the document")


def get_book_text(path):
    with open(path, "r") as fl:
        book = fl.read()
    return book


if __name__ == "__main__":
    main()
