def word_count(text):
    words = text.split()
    return len(words)


def count_characters (text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def chars_to_sorted_list (char_dict):
    sorted_chars = []

    for char, count in char_dict.items():
        char_data = {"char": char, "count": count}
        sorted_chars.append(char_data)

    def sort_on (dict):
        return dict["count"]

    sorted_chars.sort(reverse = True, key=sort_on)

    return sorted_chars 
