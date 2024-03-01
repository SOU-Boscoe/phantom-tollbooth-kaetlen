import phantom_tollbooth
def main():
    book = phantom_tollbooth.get_text()
    book = book.replace('\n','').replace('.','').replace(',','').replace('!','').replace('?','').replace(':','').replace(';','').replace('(','').replace(')','').replace('[','').replace(']','')
    book = book.replace('{','').replace('}','').replace('\'','').replace('\"','').replace('-','').replace('_','').replace('`','').replace('~','').replace('@','').replace('#','').replace('$','')
    book = book.replace('%','').replace('^','').replace('&','').replace('*','').replace('+','').replace('=','').replace('<','').replace('>','').replace('/','').replace('\\','').replace('|','')
    book = book.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').lower()
    book = book.split(' ')
    for nulls in range(book.count('')):
     book.remove('')
    book.sort()
    #print(book)
    words = {}
    for word in book:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    words=sorted(words.items(), key=lambda x: x[1], reverse=True)
    top_words = words[:50]
    print(top_words)
    print(book)
if __name__ == '__main__':
    main()