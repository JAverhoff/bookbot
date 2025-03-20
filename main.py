from stats import word_count, count_characters, chars_to_sorted_list
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

    char_counts = count_characters(book_text)
    print (char_counts)

    char_counts = count_characters(book_text)
    sorted_chars = chars_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")

    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")



































if __name__ == "__main__":
    main()