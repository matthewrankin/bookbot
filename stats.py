def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(characters):
    return characters["num"]


def sort_characters(characters):
    characters_list = []
    for k, v in characters.items():
        characters_list.append({"char": k, "num": v})
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list
