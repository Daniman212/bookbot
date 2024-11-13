def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    num_words = get_words(text)
    print(f"{num_words} words in this document")

    chars_count = get_chars(text)

    chars_sorted = chars_count_sorted(chars_count)

    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    chars ={}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_count_sorted(num_chars):
    sorted_list = []
    for ch in num_chars:
        sorted_list.append({"char": ch, "num": num_chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    
main()