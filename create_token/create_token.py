import argparse
import codecs
import os
import sentencepiece as spm
def read_dict(path_dict):
    data = list()
    with codecs.open(path_dict, "r",
                     encoding="utf8") as f_in:
        for word in f_in.read().splitlines():
            data.append(word)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--process", help="# of process for Multiprocessing", default=8, type=int
    )
    parser.add_argument("-t","--text", help="file text", default="text.txt",
                        type=str)
    parser.add_argument("-d","--dict", help="file dict", default="dict.txt",
                        type=str)
    parser.add_argument("--wp", help="number of word pieces", default=5000, type=int)
    parser.add_argument(
        "--nbest",
        help="number of best segmentations for each word (or numbers comma separated)",
        default="10",
    )
    args = parser.parse_args()

    am_path = "am"
    os.makedirs(am_path, exist_ok=True)
    # Generating am/*
    num_word_pieces = args.wp
    train_all_text = args.text
    dict_file = args.dict
    prefix = "train-all-unigram-{}".format(num_word_pieces)
    prefix = os.path.join(am_path, prefix)
    vocab_name = prefix + ".vocab"
    model_name = prefix + ".model"
    # subpaths = {
    #     "train_vlsp": ["for_train_vlsp"],
    #     "test_vlsp": ["for_test_vlsp"],
    #     "train_vindata": ["for_train_vindata"]
    # }
    # prepare data
    print("Preparing tokens and lexicon for acoustic model...\n", flush=True)
    # word_dict = defaultdict(set)
    # take
    # for key, names in subpaths.items():
    #     for name in names:
    #         with open(os.path.join(lists_path, name + ".lst"), "r") as flist:
    #             for line in flist:
    #                 transcription = line.strip().split(" ")[3:]
    #                 word_dict[key].update(transcription)
    # lexicon_words = sorted(word_dict["train_vlsp"] | word_dict["test_vlsp"]
    #                        | word_dict["train_vindata"])
    lexicon_words = read_dict(dict_file)
    print(len(lexicon_words))

    print("Computing word pieces...\n", flush=True)
    train_cmd = (
        "--input={input} --model_prefix={prefix} --vocab_size={sz}"
        " --character_coverage=1.0 --model_type=unigram --input_sentence_size=5000000"
        " --split_by_unicode_script=false --shuffle_input_sentence=true".format(
            input=train_all_text, prefix=prefix, sz=num_word_pieces
        )
    )
    spm.SentencePieceTrainer.Train(train_cmd)

    # word piece dictionary
    print("Creating word piece list...\n", flush=True)
    exclude_list = {"<unk>", "<s>", "</s>"}
    with open(vocab_name.replace(".vocab", ".tokens"), "w") as fvocab_filt:
        with open(vocab_name, "r", encoding="utf-8") as fvocab:
            for line in fvocab:
                val, _ = line.strip().split("\t", 1)
                if val not in exclude_list:
                    fvocab_filt.write(val.replace("\u2581", "_") + "\n")


    # word -> word piece lexicon for loading targets
    print("Creating word -> word pieces lexicon...\n", flush=True)
    sp = spm.SentencePieceProcessor()
    sp.Load(model_name)

    for nbest in args.nbest.split(","):
        nbest = int(nbest)
        lexicon_name = "unigram-{sz}-nbest{n}.lexicon".format(
            sz=num_word_pieces, n=nbest
        )
        with open(os.path.join(am_path, lexicon_name), "w") as f_lexicon:
            for word in lexicon_words:
                wps = sp.NBestEncodeAsPieces(word, nbest)
                for wp in wps:  # the order matters for our training
                    f_lexicon.write(
                        word
                        + "\t"
                        + " ".join([w.replace("\u2581", "_") for w in wp])
                        + "\n"
                    )
    print("Done!", flush=True)
