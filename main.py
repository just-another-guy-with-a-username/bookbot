def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num = get_words(text)
    nol = get_nol(text)
    print(f"my report on {book_path}:")
    print(f"word counting is a fun task. This one has {num} words.")
    print(f"letter counting and sorting a list of dictionaries in this fashion was kinda torturous. Here are the totals:")
    for i in range(0, len(nol)):
        for key in nol[i]:
            if key == "q":
                print(f"{key} count: {nol[i][key]} (everyone's favorite letter in scrabble)")
            elif key == "u":
                print(f"{key}wu (u) count: {nol[i][key]}")
            else:
                print(f"{key} count: {nol[i][key]}")
    print("thanks for reading the report (UwU)")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    split_up = text.split()
    return len(split_up)

def sorter(dict):
    for key in dict:
        num = dict[key]
    return num

def get_nol(text):
    list_of_dicts = []
    lower_text = text.lower()
    letters = list(lower_text)
    for letter in letters:
        if letter.isalpha():
            if any(letter in d for d in list_of_dicts):
                for i in range(0, len(list_of_dicts)):
                    if letter in list_of_dicts[i]:
                        list_of_dicts[i][letter] += 1
            else:
                list_of_dicts.append({letter: 1})
        list_of_dicts.sort(reverse=True, key=sorter)
    return list_of_dicts

main()