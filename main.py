import sys

from stats import count_characters, get_num_words, sort_character_counts


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(filepath):
    print('============ BOOKBOT ============')

    print(f'Analyzing book found at {filepath}...')
    file_contents = get_book_text(filepath)

    print('----------- Word Count ----------')
    num_words = get_num_words(file_contents)
    print(f'Found {num_words} total words')

    print('--------- Character Count -------')
    char_counts = count_characters(file_contents)
    sorted_char_counts_list = sort_character_counts(char_counts)
    for char_data in sorted_char_counts_list:
        letter = list(char_data.keys())[0]
        count = list(char_data.values())[0]
        if not letter.isalpha():
            continue
        print(f'{letter}: {count}')

    print('============= END ===============')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = sys.argv[1]
    main(filepath)
