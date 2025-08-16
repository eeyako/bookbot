def get_num_words(text: str):
    return len(text.split())


def count_characters(text: str):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def sort_character_counts(char_counts):
    char_counts_list = []
    for letter, count in char_counts.items():
        char_counts_list.append({letter: count})

    char_counts_list.sort(reverse=True, key=lambda n: list(n.values())[0])
    return char_counts_list
