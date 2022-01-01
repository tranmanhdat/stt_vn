import codecs
import os
import random
import sys


root = sys.argv[1]
out = sys.argv[2]
os.makedirs(out,exist_ok=True)

for file in os.listdir(root):
    path = os.path.join(root, file)
    f_in = codecs.open(path, "r", encoding="utf-8")
    data = f_in.readlines()
    random.shuffle(data)
    train = 1
    test = 1
    pre = file.split(".")[0]
    f_train = codecs.open(os.path.join(out, "for_train_"+file), "w+", encoding="utf-8")
    f_test = codecs.open(os.path.join(out, "for_test_"+file), "w+", encoding="utf-8")
    index_test = int(0.7 * len(data))
    for i in range(0, len(data)):
        elements = data[i].split("\t")
        if i<index_test:
            elements[0] = pre + "_train_" + str(train)
            # elements[1] = elements[1].replace("/root/src/data", "/content/drive/MyDrive/NLP-Speech2Text/data")
            train = train + 1
            data[i] = "\t".join(elements)
            f_train.write(data[i])
        else:
            elements[0] = pre + "_test_" + str(test)
            # elements[1] = elements[1].replace("/root/src/data", "/content/drive/MyDrive/NLP-Speech2Text/data")
            data[i] = "\t".join(elements)
            f_test.write(data[i])
            test = test + 1
    f_train.close()
    f_test.close()
    f_in.close()
