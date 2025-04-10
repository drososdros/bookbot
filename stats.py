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
