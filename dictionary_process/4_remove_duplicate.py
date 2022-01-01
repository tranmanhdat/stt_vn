

if __name__ == '__main__':
    last_word = None
    f_read = open("dictionary_3.txt", "r", encoding="UTF-8")
    f_write = open("dictionary_4.txt", "w+", encoding="UTF-8")
    for line in f_read:
        word = line.rstrip()
        if (last_word is not None) and word==last_word:
            continue
        f_write.write(word+"\n")
        last_word = word
