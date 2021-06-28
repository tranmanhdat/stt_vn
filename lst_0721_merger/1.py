data = open("text.txt", "r", encoding="utf8")
f_write = open("text_.txt", "w+", encoding="utf8")
for line in data:
    if len(line.rstrip()) > 2:
        f_write.write(line)