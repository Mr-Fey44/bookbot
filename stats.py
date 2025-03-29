def count_words(file_contents): #takes a string as an input and outputs an integer of the word count.
    word_count = file_contents.split()
    #print(word_count)
    return len(word_count)

def count_char(file_contents): #takes a string as an input and outputs a dictionary of each character and its count
    characters = {}
    lower_case = file_contents.lower()
    for char in lower_case:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    #print(characters)
    return characters

def sort(chars_dict):
    # Create a list of dictionaries from your character dictionary
    chars_list = []
    for char, count in chars_dict.items():
        if char.isalpha() == True:
            chars_list.append({"char": char, "count": count})

    # Sort the list in place
    chars_list.sort(reverse=True, key=lambda dict_item: dict_item["count"])

    # Return the sorted list
    return chars_list
