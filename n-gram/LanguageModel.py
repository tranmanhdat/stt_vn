class LanguageModel:
    def __init__(self):
        self.number_1_gram = 0
        self.number_2_gram = 0
        self.number_3_gram = 0
        self.list_1_grams = []
        self.list_2_grams = []
        self.list_3_grams = []
    def read_arpa(self, arpa_file):
        f_read = open(arpa_file, "r", encoding="UTF-8")
        count = 0
        while True:
            line = f_read.readline()
            if not line:
                break
            count = count + 1
            if count == 1:
                continue
            if count == 2:
                self.number_1_gram = int(line.rstrip().split("=")[-1])
            elif count == 3:
                self.number_2_gram = int(line.rstrip().split("=")[-1])
            elif count == 4:
                self.number_3_gram = int(line.rstrip().split("=")[-1])
            else:
                if line.__contains__("1-grams"):
                    while True:
                        line = f_read.readline().rstrip()
                        if len(line) > 1:
                            self.list_1_grams.append(line)
                        else:
                            break
                if line.__contains__("2-grams"):
                    while True:
                        line = f_read.readline().rstrip()
                        if len(line) > 1:
                            self.list_2_grams.append(line)
                        else:
                            break
                if line.__contains__("3-grams"):
                    while True:
                        line = f_read.readline().rstrip()
                        if len(line) > 1:
                            self.list_3_grams.append(line)
                        else:
                            break
        print(self.number_1_gram)
        print(self.number_2_gram)
        print(self.number_3_gram)
    def add_1_gram(self, words):
        print("adding {}".format(words))
        for line in self.list_1_grams:
            gram = line.split("\t")[1]
            if gram in words:
                words = list(filter(lambda a: a != gram, words))
        self.number_1_gram = self.number_1_gram + len(words)
        for word in words:
            self.list_1_grams.append("-3.0\t"+word+"\t-1.0")
    def add_2_gram(self, grams, add_1_gram=False):
        print("adding {}".format(grams))
        words = []
        add_grams = grams.copy()
        for gram in grams:
            elements = gram.split(" ")
            words = words + elements
            if elements[0]!="<s>":
                add_grams.append("<s> "+elements[0])
            if elements[1]!="</s>":
                add_grams.append(elements[1]+" </s>")
        if add_1_gram:
            unique_words = set(words)
            words = list(unique_words)
            self.add_1_gram(words)
        unique_grams = set(add_grams)
        add_grams = list(unique_grams)
        for line in self.list_2_grams:
            gram = line.split("\t")[1]
            if gram in add_grams:
                add_grams = list(filter(lambda a: a != gram, add_grams))
        self.number_2_gram = self.number_2_gram + len(add_grams)
        for gram in add_grams:
            self.list_2_grams.append("-3.0\t"+gram+"\t-1.0")
    def add_3_gram(self, grams, add_lower_grams=True):
        print("adding {}".format(grams))
        words = []
        list_2_grams = []
        add_grams = grams.copy()
        for gram in grams:
            elements = gram.split(" ")
            words = words + elements
            list_2_grams.append("<s> " + elements[0])
            list_2_grams.append(elements[0]+" " + elements[1])
            list_2_grams.append(elements[1]+" " + elements[2])
            list_2_grams.append(elements[2] + " </s>")
            if elements[0]!="<s>":
                add_grams.append("<s> " + elements[0]+" "+elements[1])
            if elements[2]!="</s>":
                add_grams.append(elements[1]+" "+elements[2]+" "+" </s>")
        if add_lower_grams:
            unique_words = set(words)
            words = list(unique_words)
            self.add_1_gram(words)
            unique_list_2_grams = set(list_2_grams)
            list_2_grams = list(unique_list_2_grams)
            self.add_2_gram(list_2_grams, add_1_gram=False)
        unique_grams = set(add_grams)
        add_grams = list(unique_grams)
        for line in self.list_2_grams:
            gram = line.split("\t")[1]
            if gram in add_grams:
                add_grams = list(filter(lambda a: a != gram, add_grams))
        self.number_3_gram = self.number_3_gram + len(add_grams)
        for gram in add_grams:
            self.list_3_grams.append("-2.5\t" + gram)

if __name__ == '__main__':
    lm = LanguageModel()
    lm.read_arpa("text_v3.arpa")
    print(lm.list_1_grams[-5:])
    print(lm.list_2_grams[-7:])
    print(lm.list_3_grams[-7:])
    lm.add_3_gram(["a b c","b b c","a b b", "a c c"])
    print(lm.list_1_grams[-5:])
    print(lm.list_2_grams[-7:])
    print(lm.list_3_grams[-7:])
