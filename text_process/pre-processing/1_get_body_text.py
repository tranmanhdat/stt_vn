import json
import os
import bs4
import argparse
from tqdm import tqdm
import mmap
import hashlib
import multiprocessing

def get_content(line):
    """
    Get the content of the line
    """
    data = json.loads(line)
    text = bs4.BeautifulSoup(data['body'], 'html.parser').get_text()
    text = text.strip()
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get body text from jsonl files')
    parser.add_argument('-i', '--input_folder', help='Input folder', required=True)
    parser.add_argument('-o', '--output_folder', help='Output folder', required=True)
    parser.add_argument('-np', '--number_paragraphs', help='Number paragraph per output text file', default=100000, type=int)
    parser.add_argument('-s', '--number_paragraphs_process', help='Number paragraph each process', default=100000, type=int)
    parser.add_argument('-n', '--number_processes', help='Number processes', default=4, type=int)
    args = parser.parse_args()
    os.makedirs(args.output_folder, exist_ok=True)
    number_paragrap = 0
    output_file = os.path.join(args.output_folder, str(int(number_paragrap/args.number_paragraphs))+'.txt')
    f_write = open(output_file, 'w+', encoding='utf-8')
    short_output = os.path.join(args.output_folder, 'short_para.txt')
    f_short_write = open(short_output, "w+", encoding='utf-8')
    # dict_hash = dict()
    # hex_digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
    # index = dict_hash.get(hex_digest, None)
    # if index is not None:
    #     continue
    # else:
    #     dict_hash[hex_digest] = 1
    for i in range(0,20):
        list_lines = []
        print("Processing file: {0}-{1}".format(i, i+1))
        file_path = os.path.join(args.input_folder, str(str(i)+'-'+str(i+1)))
        with open(file_path, 'r', encoding='utf-8') as json_file:
            with tqdm(total=os.path.getsize(file_path)) as pbar:
                for line in json_file:
                    pbar.update(len(line.encode('utf-8')))
                    list_lines.append(line)
                    if len(list_lines) == args.number_paragraphs_process:
                        with multiprocessing.Pool(processes=args.number_processes) as pool:
                            texts = pool.map(get_content, list_lines)
                        for text in texts:
                            if len(text)>10: # to avoid empty lines
                                f_write.write(text+"\n")
                                number_paragrap = number_paragrap + 1
                                if number_paragrap%args.number_paragraphs == 0:
                                    f_write.close()
                                    output_file = os.path.join(args.output_folder, str(int(number_paragrap/args.number_paragraphs))+'.txt')
                                    f_write = open(output_file, 'w+', encoding='utf-8')
                            elif len(text)>0:
                                f_short_write.write(text+"\n")
                        list_lines.clear()
        print("Total Number paragraphs: {0}".format(number_paragrap))