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
save_dir = sys.argv[2]
ratio = 0.7
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f_train = open(os.path.join(save_dir, "train.lst"), "w+")
f_test = open(os.path.join(save_dir, "test.lst"), "w+")
f_text = open(os.path.join(save_dir, "text.txt"), "w+")
filenames = os.listdir(lst_dir)
train_idx = 0
test_idx = 0
total_time = 0
unknown_words = []
for filename in filenames:
    if not filename.__contains__(".lst"):
        continue
    print("PROCESS", filename)
    f_write_train = open(os.path.join(save_dir, "train_"+filename), "w+")
    f_write_test = open(os.path.join(save_dir, "test_"+filename), "w+")
    pre_id = filename.split(".")[0]
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    length = len(lines)
    index = shuffle(list(range(length)))
    train_idxs = index[:int(length*ratio)]
    test_idxs = index[int(length*ratio):]
    train_lines = [lines[i] for i in train_idxs]
    test_lines = [lines[i] for i in test_idxs]
    for line in train_lines:
        elements = line.split("\t")
        elements[0] = "train_" + str(train_idx)
        accept = True
        for word in elements[3].rstrip().split():
            if word not in dictionary:
                unknown_words.append(word)
                accept = False
        if not accept or float(elements[2])<0.5:
            continue
        line = "\t".join(elements)
        f_train.write(line)
        elements[0] = pre_id+ "_train_" + str(train_idx)
        line = "\t".join(elements)
        f_write_train.write(line)
        f_text.write(elements[3])
        train_idx += 1
        total_time = total_time + float(elements[2])
    for line in test_lines:
        elements = line.split("\t")
        elements[0] = "test_" + str(test_idx)
        accept = True
        for word in elements[3].rstrip().split():
            if word not in dictionary:
                accept = False
                break
        if not accept or float(elements[2])<0.5:
            continue
        line = "\t".join(elements)
        f_test.write(line)
        elements[0] = pre_id+ "_test_" + str(train_idx)
        line = "\t".join(elements)
        f_write_test.write(line)
        f_text.write(elements[3])
        test_idx += 1
        total_time = total_time + float(elements[2])
    # break
f_unknown = open(os.path.join(save_dir, "unknown.txt"), "w+")
set_unknown = set(unknown_words)
list_unknown = list(set_unknown)
for word in list_unknown:
    f_unknown.write(word+"\n")
print(train_idx)
print(test_idx)
print("time train {:.2f} hours".format(total_time/3600))