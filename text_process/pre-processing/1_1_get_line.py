import json
import os
import bs4
import argparse
from tqdm import tqdm
import mmap

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get body text from jsonl files')
    parser.add_argument('-i', '--input_folder', help='Input folder', required=True)
    parser.add_argument('-o', '--output_folder', help='Output folder', required=True)
    parser.add_argument('-np', '--number_paragraphs', help='Number paragraph per output text file', default=10000, type=int)
    args = parser.parse_args()
    os.makedirs(args.output_folder, exist_ok=True)
    number_paragrap = 0
    output_file = os.path.join(args.output_folder, 'statistic.txt')
    f_write = open(output_file, 'w+', encoding='utf-8')
    for i in range(0,20):
        print("Processing file: {0}-{1}".format(i, i+1))
        file_path = os.path.join(args.input_folder, str(str(i)+'-'+str(i+1)))
        with open(file_path, 'r', encoding='utf-8') as json_file:
            j = 0
            for line in json_file:
                i = i + 1
            f_write.write("{0}\t{1}".format(file_path,j))