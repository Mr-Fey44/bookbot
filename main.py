from stats import count_words, count_char, sort
import sys

def get_book_text(file_path): #Takes a file path as an input and returns thecontents of the file as a string.
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    characters = count_char(file_contents)
    #print(f'{count_words(file_contents)} words found in the document')
    sorted_list = sort(characters)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {count_words(file_contents)} total words')
    print('--------- Character Count -------')
    for char in sorted_list:
        print(f'{char["char"]}: {char["count"]}')

main()
