import sys

from stats import get_char_count, get_num_words, sort_characters


def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    book = get_book_text(filename)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_characters(get_char_count(book))
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
