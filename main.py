def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_char(text)

    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    #Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    char_list.sort(reverse=True, key=sort_on)

    #sorts the list and prints it
    for char_dict in char_list:
        print (f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
# returns the path for the book as a string

def count_words(text):
    words = text.split()
    return len(words)
# counts the words and returns them

def count_char(text):
    char_dict = {}
    lowercase = text.lower()
    for char in lowercase:
        char_dict[char] = char_dict.get(char, 0) + 1
    return(char_dict)
# returns the count for each character, counts lowercase and capitals as the same

def sort_on(char_count):
    return char_count["num"]



main()
