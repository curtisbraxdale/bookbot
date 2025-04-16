def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_characters(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def filter_letters(char_count):
    return {char: count for char, count in char_count.items() if char.isalpha()}

def sort_char_counts(char_count):
    char_count = filter_letters(char_count)
    sorted_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_list:
        print(f"{char}: {count}")
    return
