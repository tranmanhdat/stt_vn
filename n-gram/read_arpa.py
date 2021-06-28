import sys
from LanguageModel import LanguageModel


if __name__ == '__main__':
    arpa_file = sys.argv[1]
    number_1_gram, number_2_gram, number_3_gram, list_1_grams, list_2_grams, list_3_grams = read_arpa(arpa_file)
