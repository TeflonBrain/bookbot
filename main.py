from stats import count_chars, sort_characters, report
import sys

if len(sys.argv) !=2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path, encoding="utf-8") as f: 
        file_contents = f.read()
    return file_contents
 
def main():
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    
    # Calculate word count
    words = text.split()
    word_count = len(words)
    
    char_counts = count_chars(text)
    sorted_chars = sort_characters(char_counts)
    
    # Pass path and word count to report
    report(sorted_chars, path_to_file, word_count)

main()
