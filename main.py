from stats import get_book_text
from stats import count_characters
from stats import sort_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = len(book_text.split())
    # Old code
    #print(f"{num_words} words found in the document")
    #print(count_characters(book_text))
    # New Code
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(sort_char_counts(count_characters(book_text)))
    print("============= END ===============")

main()
