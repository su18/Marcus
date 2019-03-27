#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import string
from ModuleTrain.Training import *
from sklearn.feature_extraction.text import TfidfVectorizer


class Detector(TfidfVectorizer):

    def __init__(self, input_string):
        super().__init__(smooth_idf=True, use_idf=True, analyzer='char', ngram_range=(2, 2),
                         max_df=0.85, min_df=1, lowercase=False, vocabulary=self.vocabulary_iter())
        self.input_string = [input_string]
        self.fit_vector = None
        self.model = None
        self.load_model()
        self.vectorizer()

    def load_model(self):
        # 加载模型
        with open("E:/PY-Study/XssFilter/ModuleTrain/cache/model.pkl", 'rb') as file:
            self.model = pickle.load(file)

    def vectorizer(self):
        # 字符串向量化
        self.fit_vector = self.fit_transform(self.input_string)

    def xss_predict(self):
        return self.model.predict(self.fit_vector)

    @staticmethod
    def vocabulary_iter():
        for i in string.printable:
            for j in string.printable:
                yield i + j


if __name__ == '__main__':
    xss = Detector(input_string="<>")
    result = xss.xss_predict()
    print(result)
