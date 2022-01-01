import os, sys, shutil

if __name__ == '__main__':
    file_in = sys.argv[1]
    folder_out = sys.argv[2]
    str_old = sys.argv[3]
    str_new = sys.argv[4]
    path_out = str_new+"_split"
    os.makedirs(path_out, exist_ok=True)
    file_out = os.path.join(folder_out, file_in.split("/")[-1])
    f_out = open(file_out, "w+", encoding="UTF-8")
    count = 1
    file = 0
    with open(file_in, "r", encoding="UTF-8") as f_in:
        for line in f_in:
            if len(line)>5:
                path_sub_folder = os.path.join(path_out, str(count))
                os.makedirs(path_sub_folder, exist_ok=True)
                src = line.rstrip().split("\t")[1].replace(str_old, str_new)
                dst = os.path.join(path_sub_folder, src.split("/")[-1])
                shutil.copyfile(src, dst)
                elements = line.rstrip().split("\t")
                elements[1] = dst.replace(str_new, str_old)
                f_out.write("\t".join(elements)+"\n")
                file = file + 1
                if file>5000:
                    count = count + 1
                    file = 0