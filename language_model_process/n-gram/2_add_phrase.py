import sys
from LanguageModel import LanguageModel


if __name__ == '__main__':
    arpa_file = sys.argv[1]
    out_file = sys.argv[2]
    add_file = sys.argv[3]
    language_model = LanguageModel()
    language_model.read_arpa(arpa_file)
    addition_phrase_1 = []
    addition_phrase_2 = []
    addition_phrase_3 = []
    with open(add_file, "r", encoding="utf8") as f_read:
        for line in f_read:
            line = " ".join(line.rstrip().split())
            if len(line.split())==1:
                addition_phrase_1.append(line)
            elif len(line.split())==2:
                addition_phrase_2.append(line)
            elif len(line.split())==3:
                addition_phrase_3.append(line)
            elif len(line.split())>3:
                elements = line.split()
                for i in range(0, len(elements)-2):
                    addition_phrase_3.append(" ".join(elements[i:i+3]))
    language_model.add_1_gram(addition_phrase_1)
    language_model.add_2_gram(addition_phrase_2, True)
    language_model.add_3_gram(addition_phrase_3)
    language_model.write_file(out_file)