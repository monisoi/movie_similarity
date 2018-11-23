#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim import corpora
from gensim import models
from scipy import spatial
import numpy as np
import csv
import sys


class SimilarMovieFinder:
    def __init__(self, train_file_name):
        self.sentences = self.load_sentences(train_file_name)

    def load_sentences(self, file_name):
        sentences = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for sentence in reader:
                sentences.append(sentence)
        return sentences

    def create_model(self):
        corpus, num_of_words = self.create_gensim_bow(self.sentences)
        corpus_tfidf = self.apply_tfidf(corpus)
        self.model = self.create_word_vectors(corpus_tfidf, num_of_words)

    def save_model(self, model_file_name):
        np.save(model_file_name, self.model)
        print('finish saving model')

    def load_model(self, model_file_name):
        self.model = np.load(model_file_name)
        print('finish loading model')

    def find(self, target_id):
        most_similar_id = self.find_most_similar_id(
            target_id, self.model)['id']
        print(self.sentences[target_id])
        print(self.sentences[most_similar_id])

    def create_gensim_bow(self, sentences):
        dictionary = corpora.Dictionary(sentences)
        dictionary.token2id
        return list(map(dictionary.doc2bow, sentences)), len(dictionary)

    def apply_tfidf(self, corpus):
        test_model = models.TfidfModel(corpus)
        return test_model[corpus]

    def create_word_vectors(self, corpus, num_of_words):
        # outputs as ndarray
        word_vectors = []
        for id_freq_pairs in corpus:
            word_vector = [0 for i in range(num_of_words)]
            for id_freq_pair in id_freq_pairs:
                word_vector[id_freq_pair[0]] = id_freq_pair[1]
            word_vectors.append(word_vector)
        return np.array(word_vectors)

    def calculate_cos_similarity(self, vector1, vector2):
        return 1 - spatial.distance.cosine(vector1, vector2)

    def find_most_similar_id(self, target_id, word_vectors):
        max = {'id': 0, 'similarity': 0}
        for index, word_vector in enumerate(word_vectors):
            if index is not target_id:
                similarity = self.calculate_cos_similarity(
                    word_vector, word_vectors[target_id])
                if similarity > max['similarity']:
                    max = {'id': index, 'similarity': similarity}
        return max


if __name__ == '__main__':
    f = SimilarMovieFinder('./train/train.csv')
    f.load_model('./model/model.npy')
    f.find(2)
