import codecs
import time
import os
if __name__ == '__main__':
    full_dict = []
    dict_root = "dictionary/Dict"
    files = os.listdir(dict_root)
    for file in files:
        dict_file = os.path.join(dict_root, file)
        f_read = open(dict_file, "r+", encoding='UTF-8')
        if file.__contains__("dict_"):
            for line in f_read:
                if len(line)>5:
                    elements = line.rstrip().split(",")
                    words = elements[0].split(" ")
                    for word in words:
                        if word.lower() not in full_dict:
                            full_dict.append(word.lower())
        else:
            for line in f_read:
                if line.rstrip().lower() not in full_dict:
                    full_dict.append(line.rstrip().lower())
    f_dict = open("dictionary/dictionary_from_Dict.txt", "w+", encoding="utf-8")
    for word in sorted(full_dict):
        f_dict.write(word + "\n")