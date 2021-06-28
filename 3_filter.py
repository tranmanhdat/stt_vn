import os
import sys
from sklearn.utils import shuffle
""" .lst dir save dir"""
def read_dict(path_dict):
    data = list()
    with open(path_dict, "r", encoding="utf8") as f_in:
        for word in f_in.read().splitlines():
            data.append(word)
    return data
dictionary = read_dict("dictionary.txt")
lst_dir = sys.argv[1]
ratio = 0.7
f_filter = open("anomaly.lst", "w+")
filenames = os.listdir(lst_dir)
train_idx = 0
test_idx = 0
total_time = 0
unknown_words = []
for filename in filenames:
    if not filename.__contains__(".lst"):
        continue
    print("PROCESS", filename)
    # f_write_lst = open(os.path.join(save_dir, filename), "w+")
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    for line in lines:
        elements = line.split("\t")
        elements[0] = "train_" + str(train_idx)
        accept = True
        for word in elements[3].rstrip().split():
            if word not in dictionary:
                unknown_words.append(word)
                accept = False
        if not accept:
            continue
        if float(elements[2])<0.5:
            line = "\t".join(elements)
            f_filter.write(line)
            elements[0] = "test_" + str(train_idx)
            line = "\t".join(elements)
            train_idx += 1
set_unknown = set(unknown_words)
list_unknown = list(set_unknown)