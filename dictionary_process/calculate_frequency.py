import codecs
import time

if __name__ == '__main__':
    exist_dict = []
    f_read = open("dictionary/dictionary_from_Dict.txt", "r+", encoding="UTf-8")
    for line in f_read:
        if len(line.rstrip()) > 1:
            exist_dict.append(line.rstrip())
    full_text = "/media/trandat/Documents/NLP_SpeechToText/dataset/corpus-full.txt"
    step_sentences = 1000
    dictionary_word = {}
    with open(full_text, "r") as f_in:
        i = 0
        start = time.time()
        for line in f_in:
            replace = {", ": " ", "\'": "", "\"": "", "[": " ", "]": " ", "?": "", "!": "", "(": " ", ")": " ",
                       "./": "", "; ": " ", ": ": " ", ",": " ", "-": " ", "/": " ", "&": " ", ":": " ", ";": " ",
                       ".": " ", "@": " ", "+": " ", "mm²": "", "_": "", "*": "", ">": "", "|": "", "=": "", "^": "",
                       "<": "", "m²": "", "³": "", "$": "", "¹": "", "¼": "", "}": "", "{": "", "λ": "", "%": "",
                       "½": "", "⅓": "", "²": "", "简中 繁中": "", "¾": "", "ü": "", "ö": "", "ак": "", "м": "", "т": "",
                       "⁰": "", "каб": "каб", "кр": "", "α": "", "①": "", "панцирь": "", "ß": "", "čė": "", "ш": "",
                       "čė": ""}
            for key in replace:
                line = line.replace(key, replace[key])
            words = line.lower().rstrip().split(' ')
            for word in words:
                if word == '.' or word in exist_dict:
                    continue
                if word not in dictionary_word:
                    dictionary_word[word] = 1
                else:
                    dictionary_word[word] = dictionary_word[word] + 1
            i = i + 1
            if i % step_sentences == 0:
                end = time.time()
                print("processed from {} to {} take {:.2f}".format(
                        i - step_sentences, i, end - start))
                start = end
                break
    with codecs.open("dictionary/frequence_dict/frequency.txt", "w+", encoding="utf-8") as f_out:
        f_dict = open("dictionary/frequence_dict/dictionary.txt", "w+", encoding="utf-8")
        for word in sorted(dictionary_word, key=dictionary_word.get,
                           reverse=True):
            f_out.write(word + '\t' + str(dictionary_word[word]) + '\r\n')
            f_dict.write(word + "\r\n")
