BOOK_FILE_PATH="books/frankenstein.txt"

def load_file():
    with open(BOOK_FILE_PATH) as f:
        file_contents = f.read()
    return file_contents

def count_words(s):
    return len(s.strip().split())

def count_chars(s):
    res = {}
    for c in s.lower():
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res

def main():
    fc = load_file()

    wc = count_words(fc)    
    cc = count_chars(fc)

    print(f"--- Begin report of {BOOK_FILE_PATH} ---")
    print(f"{wc} words found in the document")
    print("")

    for c in cc:
        print(f"The '{c}' character was found {cc[c]} times")

    print("--- End report ---")

main()
