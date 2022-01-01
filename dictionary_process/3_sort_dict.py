

if __name__ == '__main__':
    dictionary = []
    f_read = open("dictionary_2.txt", "r", encoding="UTF-8")
    for line in f_read:
        word = line.rstrip()
        if len(word)>=1:
            dictionary.append(word)
    f_write = open("dictionary_3.txt", "w+", encoding="UTF-8")
    for word in sorted(dictionary):
        f_write.write(word+"\n")

