import os
import sys
from sklearn.utils import shuffle
""" .lst dir save dir"""
lst_dir = sys.argv[1]
save_dir = lst_dir
f_static = open(os.path.join(save_dir, "static.txt"), "w+")
filenames = os.listdir(lst_dir)
total_time = 0
for filename in filenames:
    if not (filename.__contains__("test_") or  filename.__contains__("train_") ):
        continue
    print("PROCESS", filename)
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    length = len(lines)
    for line in lines:
        elements = line.split("\t")
        total_time = total_time + float(elements[2])
    hours = total_time/3600
    f_static.write(str(filename) + "\t" + str(length)+"\t"+str("{:.2f}".format(hours))+"\n")
    total_time = 0