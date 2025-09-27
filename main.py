import sys
from stats import count_words, count_characters, character_report_items

def get_book_text(filepath: str) -> str:
    with open(filepath, encoding='utf-8') as f:
        return f.read()

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(text)
    report_items = character_report_items(char_counts)
    for item in report_items:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()





