#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models.doc2vec import Doc2Vec
import sys
import csv


class SimilarMovieFinder:
    def __init__(self, train_file_name, model_file_name):
        self.sentences = self.load_sentences(train_file_name)
        self.model = Doc2Vec.load(model_file_name)

    def load_sentences(self, file_name):
        sentences = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for sentence in reader:
                sentences.append(sentence)
        return sentences

    def find(self, target_id):
        most_similar_id = self.model.docvecs.most_similar(target_id)[0][0]
        print(self.sentences[target_id])
        print(self.sentences[most_similar_id])

if __name__ == '__main__':
    train_file_name = sys.argv[1]  # ex) ./train/train.csv
    model_file_name = sys.argv[2]  # ex) ./model/model.model
    target_id = sys.argv[3]
    f = SimilarMovieFinder(train_file_name, model_file_name)
    print(f.find(int(target_id)))