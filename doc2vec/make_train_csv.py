#!/usr/bin/env python
# -*- coding: utf-8 -*-

from natto import MeCab
import csv
import sys
import glob


def make_train_csv(import_directory_name, export_file_name):
    # ディレクトリから文章を一行ずつ読み込んで単語で分割し、ファイルに出力する
    import_file_names = glob.glob('{}/*'.format(import_directory_name))
    with open(export_file_name, 'w') as export_file:
        for import_file_name in import_file_names:
            print(import_file_name)
            with open(import_file_name, 'r') as import_file:
                reader = csv.reader(import_file)
                writer = csv.writer(export_file, lineterminator='\n')
                for sentence in reader:
                    words = []
                    with MeCab() as nm:
                        for n in nm.parse(sentence[0], as_nodes=True):
                            if not n.is_eos():
                                words.append(n.surface)
                    writer.writerow(words)


if __name__ == '__main__':
    import_directory_name = sys.argv[1]  # ex) ./raw
    export_file_name = sys.argv[2]  # ex) ./train/train.csv
    make_train_csv(import_directory_name, export_file_name)
