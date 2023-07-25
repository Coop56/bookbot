def count_letter_occurrences(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def count_words(book_text):
    return len(book_text.split())

def print_book_count_report(book_path):
    with open(book_path, 'r') as file:
        book_text = file.read()

    print(f"--- Begin report of {book_path} ---")

    word_count = count_words(book_text)
    print(f"{word_count} words found in the document\n")

    char_counts = count_letter_occurrences(book_text)
    char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in char_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    print_book_count_report('books/frankenstein.txt')