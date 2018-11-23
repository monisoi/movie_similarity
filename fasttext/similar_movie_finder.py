#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models.wrappers.fasttext import FastText
from scipy import spatial
import numpy as np
import csv
import sys


class SimilarMovieFinder:
    def __init__(self, train_file_name, model_file_name):
        self.sentences = self.load_sentences(train_file_name)
        self.num_features = 300
        self.model = self.load_model(model_file_name)
        print('finish loading model')
        self.sentence_vectors = self.make_sentence_avg_feature_vectors()

    def load_sentences(self, file_name):
        sentences = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for sentence in reader:
                sentences.append(sentence)
        return sentences

    def load_model(self, model_file_name):
        return FastText.load_fasttext_format(model_file_name)

    def avg_feature_vector(self, sentence):
        feature_vec = np.zeros((self.num_features,),
                               dtype="float32")  # 特徴ベクトルの入れ物を初期化
        for word in sentence:
            try:
                word_in_model = self.model[word]
                feature_vec = np.add(feature_vec, word_in_model)
            except KeyError:
                print('{} does not exist in the model'.format(word))
        if len(sentence) > 0:
            feature_vec = np.divide(feature_vec, len(sentence))
        return feature_vec

    def make_sentence_avg_feature_vectors(self):
        sentence_vectors = []
        for index, sentence in enumerate(self.sentences):
            avg_vector = self.avg_feature_vector(sentence)
            sentence_vectors.append(
                {'index': index, 'sentence': sentence, 'vector': avg_vector})
        return sentence_vectors

    def find(self, target_id):
        most_similar_id = self.find_most_similar_id(target_id)['id']
        print(self.sentences[target_id])
        print(self.sentences[most_similar_id])

    def calculate_cos_similarity(self, vector1, vector2):
        return 1 - spatial.distance.cosine(vector1, vector2)

    def find_most_similar_id(self, target_id):
        max = {'id': 0, 'similarity': 0}
        target_sentence_vector = self.sentence_vectors[target_id]['vector']
        for index, sentence in enumerate(self.sentences):
            if index is not target_id:
                similarity = self.calculate_cos_similarity(
                    target_sentence_vector, self.sentence_vectors[index]['vector'])
                if similarity > max['similarity']:
                    max = {'id': index, 'similarity': similarity}
        return max


if __name__ == '__main__':
    f = SimilarMovieFinder('./train/train.csv', './model/wiki.ja/wiki.ja')
    f.find(0)
