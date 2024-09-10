import sys


def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        chars = [{k: v} for k, v in count_characters(file_contents).items()]
        print(f"--- Begin report of {f.name} ---")
        print_report(words, chars)
        print("--- End report ---")


def print_report(words, chars):
    chars.sort(reverse=True, key=lambda n: list(n.values())[0])
    print(f"{words} words found in the document\n")
    for char in chars:
        letter = list(char.keys())[0]
        count = list(char.values())[0]
        print(f"The '{letter}' character was found {count} times")


def count_words(text: str):
    return len(text.split())


def count_characters(text: str):
    text = text.lower()
    char_count = {}
    for char in text:
        if not char.isalpha():
            continue
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("No files were provided. Usage: python main.py {file_path}")

    filepath = sys.argv[1]
    main(filepath)
