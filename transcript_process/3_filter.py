import os
import sys
""" .lst dir save dir"""
def read_dict(path_dict):
    data = list()
    with open(path_dict, "r", encoding="utf8") as f_in:
        for word in f_in.read().splitlines():
            data.append(word)
    return data
dictionary = read_dict("dictionary.txt")
lst_dir = sys.argv[1]
save_dir = sys.argv[2]
os.makedirs(save_dir, exist_ok=True)
filenames = os.listdir(lst_dir)
unknown_words = []
for filename in filenames:
    if not filename.__contains__(".lst"):
        continue
    print("PROCESS", filename)
    f_write_lst = open(os.path.join(save_dir, filename), "w+")
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    for line in lines:
        elements = line.split("\t")
        accept = True
        for word in elements[3].rstrip().split():
            if word not in dictionary:
                unknown_words.append(word)
                accept = False
        if not accept:
            continue
        if accept:
            f_write_lst.write(line)