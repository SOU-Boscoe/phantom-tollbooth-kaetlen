import phantom_tollbooth

def main():
    book = phantom_tollbooth.get_text()
    for char in book:
        if not char.isalpha() and char != "'":
            book = book.replace(char, ' ')
    book = book.lower()
    book = book.split(' ')
    for _ in range(book.count('')):
        book.remove('')
    book.sort()
    words = {}
    for word in book:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    # print(words)
    top_words = {}
    for _ in range(50):
        top_words[max(words, key=words.get)] = words[max(words, key=words.get)]
        del words[max(words, key=words.get)]
    print(top_words)
    #print(book)


if __name__ == '__main__':
    main()