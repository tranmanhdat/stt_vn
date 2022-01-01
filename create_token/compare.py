def read_dict(path_dict):
    data = list()
    with open(path_dict, "r", encoding="utf8") as f_in:
        for word in f_in.read().splitlines():
            data.append(word)
    return data
dictionary = read_dict("dictionary.txt")
dictionary_old = read_dict("dictionary_old.txt")
oov_dictionary, oov_old = [], []
for word  in dictionary:
    if word not in dictionary_old:
        oov_old.append(word)
for word in dictionary_old:
    if word not in dictionary:
        oov_dictionary.append(word)
f_write = open("oov_dictionary.txt", "w+", encoding="utf8")
for word in oov_dictionary:
    f_write.write(word+"\n")
f_write.close()
f_write = open("oov_old.txt", "w+", encoding="utf8")
for word in oov_old:
    f_write.write(word+"\n")
f_write.close()