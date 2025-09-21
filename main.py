import sys
from stats import word_counter
from stats import char_counter
from stats import get_book_text
    

def main(filepath):
    file_contents = get_book_text(filepath)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}\n----------- Word Count ----------")
    num_words = word_counter(file_contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    report_list = char_counter(file_contents)
    for item in report_list:
        if item["char"].isalpha():
            char = item["char"]
            num = item["num"]
            print(f"{char}: {num}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])