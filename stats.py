def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

#Dict most: A vizsgált karakter a kulcs, a darabszáma pedig az érték
#Dict next: A dictonary "char" kulcsának értéke lesz a vizsgált betű. A dictonary "num" kulcsának értéke lesz a darabszám.

def sort_on(items):
    return items["num"]

def char_counter(file_contents):
    dict = {}
    report_list = []
    text = file_contents.lower()
    for char in text:
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    for char, count in dict.items():
        new_dict = {"char": char, "num": count}
        report_list.append(new_dict)
    report_list.sort(reverse=True, key=sort_on)
    return report_list

