import os , sys

if __name__ == '__main__':
    files = os.listdir("Dict")
    addition_words = []
    for file in files:
        path_file = os.path.join("Dict", file)
        f_read = open(path_file, "r", encoding="utf8")
        for line in f_read:
            elements = line.rstrip().split(",")
            phrase = " ".join(elements[-1].split(" ")).lower()
            addition_words.append(phrase)
        f_read.close()
    f_write = open("addition_phrase.txt", "w+", encoding="utf8")
    for phrase in addition_words:
        f_write.write(phrase+"\n")
    f_write.close()