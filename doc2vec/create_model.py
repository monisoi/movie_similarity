#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import sys


def create_model(train_data, model_name):
    with open(train_data, 'r') as f:
        train_corpus = [TaggedDocument(words=data.split(','), tags=[i])
                        for i, data in enumerate(f)]
        model = Doc2Vec(documents=train_corpus, dm=1,
                        vector_size=300, window=8, min_count=1, workers=4)
        model.train(train_corpus, total_examples=model.corpus_count, epochs=50)
        model.save(model_name)


if __name__ == '__main__':
    train_data = sys.argv[1]
    model_name = sys.argv[2]
    # ex. MyModel.model
    create_model(train_data, model_name)
