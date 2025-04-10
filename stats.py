def count_text_words(book):
    return len(book.split())


def count_letters(book):
    letter_occurrences = {}
    for letter in book:
        l_letter = letter.lower()
        if l_letter in letter_occurrences:
            letter_occurrences[l_letter] += 1
        else:
            letter_occurrences[l_letter] = 1
    return letter_occurrences


def stats_report(text_words, count_letters):
    print(
        """
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
"""
    )
    print(f"Found {text_words} total words")
    print("--------- Character Count -------")
    for key in sorted(count_letters):
        if key.isalpha():
            print(f"{key}: {count_letters[key]}")

    print("============= END ===============")
